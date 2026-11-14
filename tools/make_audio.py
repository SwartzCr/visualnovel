"""Synthesize the game's music and sound effects (numpy only), and encode them
to OGG Vorbis in game/audio/ with ffmpeg.

    python3 tools/make_audio.py

Music (seamless loops):
    theme.ogg    main menu: slow lounge, Fmaj7 Dm7 Gm7 C7
    day.ogg      afternoons at the indoor pool: breezy bossa electric piano
    night.ogg    hallways and art rooms: moody synthwave arpeggios
    party.ogg    the ballroom: four-on-the-floor house stabs
    tender.ogg   the roof, dawn, the ship: warm pads and a bell melody

Sound effects:
    click.ogg, rapport_up.ogg, rapport_down.ogg, night.ogg-style whoosh (whoosh.ogg)

Everything is deterministic (fixed random seeds), so re-running gives the
same files. Drop in replacements with the same names to use real music.
"""

import os
import subprocess
import tempfile
import wave

import numpy as np

SR = 44100
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "game", "audio")

NOTE = {n: i for i, n in enumerate(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])}


def hz(name):
    """'A4' -> 440.0"""
    pitch, octave = name[:-1], int(name[-1])
    return 440.0 * 2 ** ((NOTE[pitch] + 12 * (octave + 1) - 69) / 12)


def chord(root, kind, octave=3):
    steps = {"maj7": [0, 4, 7, 11], "m7": [0, 3, 7, 10], "7": [0, 4, 7, 10],
             "maj": [0, 4, 7], "min": [0, 3, 7], "6": [0, 4, 7, 9], "m9": [0, 3, 7, 10, 14],
             "add9": [0, 4, 7, 14]}[kind]
    base = hz("%s%d" % (root, octave))
    return [base * 2 ** (s / 12) for s in steps]


# ---------------------------------------------------------------- voices

def env(n, a, d, s, r, sustain_len=None):
    """ADSR envelope of n samples."""
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    e = np.full(n, s, dtype=np.float64)
    a = min(a, n)
    e[:a] = np.linspace(0, 1, a, endpoint=False) if a else e[:a]
    d_end = min(a + d, n)
    if d_end > a:
        e[a:d_end] = np.linspace(1, s, d_end - a, endpoint=False)
    if r and n > r:
        e[n - r:] *= np.linspace(1, 0, r)
    return e


def t(n):
    return np.arange(n) / SR


def epiano(f, dur, vel=0.5):
    n = int(dur * SR)
    tt = t(n)
    mod = np.sin(2 * np.pi * f * 1.0 * tt) * 1.6 * np.exp(-tt * 3)
    tone = np.sin(2 * np.pi * f * tt + mod)
    tone += 0.25 * np.sin(2 * np.pi * f * 2 * tt) * np.exp(-tt * 5)
    return vel * tone * env(n, 0.004, 0.6, 0.35, 0.25)


def pad(f, dur, vel=0.3):
    n = int(dur * SR)
    tt = t(n)
    out = np.zeros(n)
    for det in (-0.004, 0.0, 0.0045):
        ph = 2 * np.pi * f * (1 + det) * tt
        out += (2 * ((ph / (2 * np.pi)) % 1) - 1)  # saw
    out = lowpass(out / 3, 900 + f)
    return vel * out * env(n, 0.6, 0.4, 0.8, 0.8)


def pluck(f, dur, vel=0.4, bright=3000):
    n = int(dur * SR)
    tt = t(n)
    sq = np.sign(np.sin(2 * np.pi * f * tt)) * 0.6 + (2 * ((f * tt) % 1) - 1) * 0.4
    return vel * lowpass(sq, bright) * env(n, 0.002, 0.18, 0.15, 0.08)


def bell(f, dur, vel=0.35):
    n = int(dur * SR)
    tt = t(n)
    mod = np.sin(2 * np.pi * f * 3.5 * tt) * 2.2 * np.exp(-tt * 2)
    return vel * np.sin(2 * np.pi * f * tt + mod) * np.exp(-tt * 1.6) * env(n, 0.003, 0.1, 1, 0.05)


def bass(f, dur, vel=0.5):
    n = int(dur * SR)
    tt = t(n)
    tone = np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2 * f * tt)
    return vel * tone * env(n, 0.005, 0.15, 0.7, 0.06)


def kick(vel=0.9):
    n = int(0.35 * SR)
    tt = t(n)
    freq = 50 + 90 * np.exp(-tt * 30)
    ph = 2 * np.pi * np.cumsum(freq) / SR
    return vel * np.sin(ph) * np.exp(-tt * 9)


RNG = np.random.default_rng(7)


def noise(n):
    return RNG.uniform(-1, 1, n)


def snare(vel=0.4):
    n = int(0.22 * SR)
    tt = t(n)
    return vel * (highpass(noise(n), 1500) * np.exp(-tt * 18) + 0.4 * np.sin(2 * np.pi * 190 * tt) * np.exp(-tt * 25))


def hat(vel=0.18, open_=False):
    n = int((0.25 if open_ else 0.06) * SR)
    tt = t(n)
    return vel * highpass(noise(n), 7000) * np.exp(-tt * (12 if open_ else 60))


def shaker(vel=0.12):
    n = int(0.09 * SR)
    tt = t(n)
    e = np.minimum(tt / 0.02, 1) * np.exp(-tt * 35)
    return vel * highpass(noise(n), 5000) * e


# ---------------------------------------------------------------- filters / fx

def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    b = 1 - a
    for i in range(len(x)):  # one-pole, fine for our lengths
        acc = b * x[i] + a * acc
        y[i] = acc
    return y


def lowpass_fast(x, cutoff):
    from scipy.signal import butter, lfilter
    bb, aa = butter(2, cutoff / (SR / 2))
    return lfilter(bb, aa, x)


def highpass(x, cutoff):
    from scipy.signal import butter, lfilter
    bb, aa = butter(2, cutoff / (SR / 2), btype="high")
    return lfilter(bb, aa, x)


# The per-sample python lowpass is slow; use scipy everywhere.
lowpass = lowpass_fast  # noqa: F811


def reverb(x, wet=0.25, size=1.0):
    """Small Schroeder reverb: parallel combs into series allpasses."""
    from scipy.signal import lfilter
    out = np.zeros_like(x)
    for d, g in ((1557, 0.84), (1617, 0.83), (1491, 0.84), (1422, 0.83)):
        d = int(d * size)
        a = np.zeros(d + 1)
        a[0], a[d] = 1, -g
        out += lfilter([1], a, x)
    out /= 4
    for d, g in ((225, 0.5), (556, 0.5), (441, 0.5)):
        b = np.zeros(d + 1)
        b[0], b[d] = -g, 1
        a = np.zeros(d + 1)
        a[0], a[d] = 1, -g
        out = lfilter(b, a, out)
    return (1 - wet) * x + wet * out


class Track:
    def __init__(self, bpm, bars, beats=4):
        self.beat = 60.0 / bpm
        self.length = int(bars * beats * self.beat * SR)
        tail = int(4 * SR)
        self.buf = np.zeros(self.length + tail)

    def add(self, sound, at_beat, pan=0.0):
        i = int(at_beat * self.beat * SR)
        end = min(i + len(sound), len(self.buf))
        self.buf[i:end] += sound[:end - i]

    def render(self, wet=0.25, size=1.0):
        x = reverb(self.buf, wet, size)
        # Fold the tail back onto the start so the loop is seamless.
        loop = x[:self.length].copy()
        tail = x[self.length:]
        loop[:len(tail)] += tail
        return loop


# ---------------------------------------------------------------- music

def scale_notes(root, mode, low, high):
    steps = {"major_pent": [0, 2, 4, 7, 9], "minor_pent": [0, 3, 5, 7, 10],
             "dorian": [0, 2, 3, 5, 7, 9, 10], "major": [0, 2, 4, 5, 7, 9, 11]}[mode]
    out = []
    for octave in range(1, 7):
        for s in steps:
            f = hz("%s%d" % (root, octave)) * 2 ** (s / 12)
            if low <= f <= high:
                out.append(f)
    return sorted(out)


def melody(tr, notes, bars, beats_per_bar, voice, rng, start_bar=0, density=0.55, step=0.5, vel=0.3):
    idx = len(notes) // 2
    beat = start_bar * beats_per_bar
    end = (start_bar + bars) * beats_per_bar
    while beat < end:
        if rng.random() < density:
            idx = int(np.clip(idx + rng.choice([-2, -1, -1, 0, 1, 1, 2]), 0, len(notes) - 1))
            length = step * rng.choice([1, 1, 2, 3])
            tr.add(voice(notes[idx], length * tr.beat * 1.1, vel), beat)
            beat += length
        else:
            beat += step


def make_theme():
    rng = np.random.default_rng(1)
    tr = Track(84, 16)
    prog = [("F", "maj7"), ("D", "m7"), ("G", "m7"), ("C", "7")]
    for bar in range(16):
        r, k = prog[bar % 4]
        for f in chord(r, k, 3):
            tr.add(epiano(f, 2.2 * tr.beat, 0.16), bar * 4)
            tr.add(epiano(f, 1.6 * tr.beat, 0.10), bar * 4 + 2.5)
        tr.add(bass(hz("%s2" % r), 1.8 * tr.beat, 0.35), bar * 4)
        tr.add(bass(hz("%s2" % r) * 1.5, 0.9 * tr.beat, 0.25), bar * 4 + 2.5)
        for b in range(4):
            tr.add(shaker(0.05), bar * 4 + b + 0.5)
        if bar % 2 == 1:
            tr.add(snare(0.08), bar * 4 + 3)
    melody(tr, scale_notes("F", "major_pent", 330, 900), 12, 4, bell, rng, start_bar=4, density=0.4, step=0.5, vel=0.18)
    return tr.render(0.32, 1.1)


def make_day():
    rng = np.random.default_rng(2)
    tr = Track(104, 16)
    prog = [("D", "m7"), ("G", "7"), ("C", "maj7"), ("A", "m7")]
    # bossa comping pattern (in beats)
    comp = [0, 1.5, 2.5, 3.5]
    for bar in range(16):
        r, k = prog[bar % 4]
        for c in comp:
            for f in chord(r, k, 3):
                tr.add(epiano(f, 0.7 * tr.beat, 0.11), bar * 4 + c)
        root = hz("%s2" % r)
        tr.add(bass(root, 1.4 * tr.beat, 0.38), bar * 4)
        tr.add(bass(root * 1.5, 0.9 * tr.beat, 0.30), bar * 4 + 1.5)
        tr.add(bass(root, 0.9 * tr.beat, 0.30), bar * 4 + 2)
        tr.add(bass(root * 1.5, 0.9 * tr.beat, 0.28), bar * 4 + 3.5)
        for e in range(8):
            tr.add(shaker(0.09 if e % 2 else 0.05), bar * 4 + e * 0.5)
        tr.add(kick(0.35), bar * 4)
        tr.add(kick(0.25), bar * 4 + 2.5)
        tr.add(snare(0.06), bar * 4 + 1.5)  # rim-ish
    melody(tr, scale_notes("C", "major_pent", 400, 1100), 8, 4, pluck, rng, start_bar=8, density=0.5, step=0.5, vel=0.14)
    return tr.render(0.22, 0.9)


def make_night():
    rng = np.random.default_rng(3)
    tr = Track(92, 16)
    prog = [("A", "min"), ("F", "maj"), ("C", "maj"), ("G", "maj")]
    for bar in range(16):
        r, k = prog[bar % 4]
        notes = chord(r, k, 3)
        for f in notes:
            tr.add(pad(f, 4.1 * tr.beat, 0.10), bar * 4)
        arp = notes + [notes[0] * 2, notes[1] * 2]
        for s in range(16):
            f = arp[[0, 1, 2, 3, 2, 1, 4, 2][s % 8]] * 2
            tr.add(pluck(f, 0.22 * tr.beat, 0.09, bright=2200), bar * 4 + s * 0.25)
        tr.add(bass(hz("%s1" % r) * 2, 1.9 * tr.beat, 0.36), bar * 4)
        tr.add(bass(hz("%s1" % r) * 2, 1.9 * tr.beat, 0.30), bar * 4 + 2)
        if bar >= 4:
            tr.add(kick(0.45), bar * 4)
            tr.add(kick(0.45), bar * 4 + 2)
            tr.add(snare(0.16), bar * 4 + 1)
            tr.add(snare(0.16), bar * 4 + 3)
            for e in range(8):
                tr.add(hat(0.05), bar * 4 + e * 0.5 + 0.25)
    melody(tr, scale_notes("A", "minor_pent", 330, 880), 8, 4, bell, rng, start_bar=8, density=0.35, step=0.5, vel=0.14)
    return tr.render(0.35, 1.3)


def make_party():
    rng = np.random.default_rng(4)
    tr = Track(122, 16)
    prog = [("D", "m7"), ("G", "7"), ("C", "maj7"), ("A", "m7")]
    for bar in range(16):
        r, k = prog[bar % 4]
        for b in range(4):
            tr.add(kick(0.75), bar * 4 + b)
            tr.add(hat(0.12, open_=True), bar * 4 + b + 0.5)
            tr.add(hat(0.05), bar * 4 + b + 0.25)
            tr.add(hat(0.05), bar * 4 + b + 0.75)
        tr.add(snare(0.22), bar * 4 + 1)
        tr.add(snare(0.22), bar * 4 + 3)
        for st in (0.5, 1.75, 2.5, 3.75):
            for f in chord(r, k, 4):
                tr.add(pluck(f, 0.3 * tr.beat, 0.06, bright=3500), bar * 4 + st)
        root = hz("%s2" % r)
        for b in range(4):
            tr.add(bass(root, 0.4 * tr.beat, 0.34), bar * 4 + b + 0.5)
        if bar % 4 == 0:
            for f in chord(r, k, 3):
                tr.add(pad(f, 16 * tr.beat, 0.05), bar * 4)
    melody(tr, scale_notes("D", "dorian", 440, 1200), 8, 4, bell, rng, start_bar=8, density=0.45, step=0.25, vel=0.10)
    return tr.render(0.18, 0.8)


def make_tender():
    rng = np.random.default_rng(5)
    tr = Track(70, 12)
    prog = [("C", "maj7"), ("A", "m7"), ("F", "maj7"), ("G", "6")]
    for bar in range(12):
        r, k = prog[bar % 4]
        for f in chord(r, k, 3):
            tr.add(pad(f, 4.2 * tr.beat, 0.11), bar * 4)
        for i, f in enumerate(chord(r, k, 4)):
            tr.add(epiano(f, 2.5 * tr.beat, 0.07), bar * 4 + i * 0.5)
        tr.add(bass(hz("%s2" % r), 3.8 * tr.beat, 0.25), bar * 4)
    melody(tr, scale_notes("C", "major_pent", 500, 1400), 12, 4, bell, rng, density=0.32, step=1.0, vel=0.16)
    return tr.render(0.45, 1.5)


# ---------------------------------------------------------------- sfx

def sfx_click():
    n = int(0.08 * SR)
    tt = t(n)
    return 0.5 * np.sin(2 * np.pi * 1400 * tt) * np.exp(-tt * 70) + 0.2 * highpass(noise(n), 3000) * np.exp(-tt * 120)


def sfx_rapport_up():
    out = np.zeros(int(0.9 * SR))
    for i, f in enumerate((hz("C6"), hz("E6"), hz("G6"))):
        s = bell(f, 0.7, 0.35)
        j = int(i * 0.07 * SR)
        out[j:j + len(s)] += s[:len(out) - j]
    return reverb(out, 0.3, 0.7)


def sfx_rapport_down():
    out = np.zeros(int(0.8 * SR))
    for i, f in enumerate((hz("E5"), hz("C5"))):
        s = epiano(f, 0.5, 0.35)
        j = int(i * 0.12 * SR)
        out[j:j + len(s)] += s[:len(out) - j]
    return reverb(out, 0.25, 0.7)


def sfx_whoosh():
    n = int(1.4 * SR)
    tt = t(n)
    x = noise(n)
    from scipy.signal import butter, lfilter
    out = np.zeros(n)
    # sweep a bandpass up and back down
    for i, seg in enumerate(np.array_split(np.arange(n), 28)):
        c = 400 + 3000 * np.sin(np.pi * (i + 0.5) / 28)
        bb, aa = butter(2, [c * 0.7 / (SR / 2), min(c * 1.4, SR / 2 - 100) / (SR / 2)], btype="band")
        out[seg] = lfilter(bb, aa, x)[seg]
    e = np.sin(np.pi * tt / tt[-1]) ** 2
    return reverb(0.5 * out * e, 0.3, 1.2)


def sfx_ark():
    """The ark at 11:11: a rising shimmering swell."""
    n = int(5.0 * SR)
    tt = t(n)
    out = np.zeros(n)
    for f in chord("C", "add9", 3) + chord("C", "add9", 4):
        rise = f * (0.5 + 0.5 * np.minimum(tt / 3.5, 1))
        out += np.sin(2 * np.pi * np.cumsum(rise) / SR) * 0.12
    out *= np.minimum(tt / 3.5, 1) ** 2 * np.exp(-np.maximum(tt - 3.8, 0) * 2.5)
    out += 0.08 * highpass(noise(n), 6000) * np.minimum(tt / 3.5, 1) ** 3 * np.exp(-np.maximum(tt - 3.8, 0) * 3)
    return reverb(out, 0.45, 1.6)


# ---------------------------------------------------------------- output

def stereo(x, width=0.0):
    if width:
        d = int(0.012 * SR)
        r = np.concatenate([x[-d:], x[:-d]])
        return np.stack([x, (1 - width) * x + width * r], axis=1)
    return np.stack([x, x], axis=1)


def write_ogg(name, x, peak=0.7, width=0.35, quality=4):
    x = x / max(np.abs(x).max(), 1e-9) * peak
    data = (stereo(x, width) * 32767).astype(np.int16)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        tmp = f.name
    with wave.open(tmp, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())
    path = os.path.join(OUT, name)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-c:a", "libvorbis",
                    "-q:a", str(quality), path], check=True)
    os.remove(tmp)
    print("wrote", os.path.relpath(path, ROOT), "%.1fs" % (len(x) / SR), "%d KB" % (os.path.getsize(path) // 1024))


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "sfx"), exist_ok=True)
    write_ogg("theme.ogg", make_theme(), 0.6)
    write_ogg("day.ogg", make_day(), 0.6)
    write_ogg("night.ogg", make_night(), 0.6)
    write_ogg("party.ogg", make_party(), 0.62)
    write_ogg("tender.ogg", make_tender(), 0.55)
    write_ogg("sfx/click.ogg", sfx_click(), 0.4, 0)
    write_ogg("sfx/rapport_up.ogg", sfx_rapport_up(), 0.5, 0.2)
    write_ogg("sfx/rapport_down.ogg", sfx_rapport_down(), 0.45, 0.2)
    write_ogg("sfx/whoosh.ogg", sfx_whoosh(), 0.45, 0.4)
    write_ogg("sfx/ark.ogg", sfx_ark(), 0.6, 0.4)
