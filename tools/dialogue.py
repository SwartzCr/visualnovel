"""Export all of the game's dialogue to one editable markdown file, and apply
edits from that file back to the .rpy scripts.

    python3 tools/dialogue.py export [DIALOGUE.md]
    python3 tools/dialogue.py import [DIALOGUE.md]

Every editable line in the markdown starts with a tag like `juni:42`, which
is the file and line number it came from. Importing:

- changes the text (and the speaker or expression) of every tagged line
- deletes the dialogue lines whose tagged line was removed (choices are kept)
- inserts new untagged lines after the tagged line above them

Lines starting with ">" are context (scene changes, menus, rapport) and are
ignored on import. Import must run on the same version of the scripts that
was exported, because the tags are line numbers. The commit is recorded in
the file's header, so edits to an older export can be applied on that commit
and merged forward with git.
"""

import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(ROOT, "game")
FILES = ["script", "juni", "gerald", "solstice", "wren", "zyx", "encounters", "finale"]
DEFAULT_MD = os.path.join(ROOT, "DIALOGUE.md")

GUEST_NAMES = {"juni": "Juni", "gerald": "Gerald", "solstice": "Solstice", "wren": "Wren", "zyx": "Zyx"}

STATEMENT_WORDS = {
    "scene", "show", "hide", "with", "play", "stop", "queue", "pause", "jump", "call",
    "return", "menu", "if", "elif", "else", "while", "pass", "label", "define", "default",
    "init", "python", "image", "transform", "screen", "style", "window", "nvl", "voice",
}


# ---------------------------------------------------------------- helpers

def load_characters():
    """Map Ren'Py character variable -> display name, from core.rpy."""
    chars = {}
    for line in open(os.path.join(GAME, "core.rpy"), encoding="utf-8"):
        m = re.match(r'define (\w+) = Character\((.*)', line)
        if not m:
            continue
        var, args = m.groups()
        name = re.search(r'name="([^"]*)"', args) or re.match(r'\s*"([^"]*)"', args)
        if name:
            chars[var] = name.group(1)
    return chars


def string_end(s, start):
    """Index just past the closing quote of the string literal at s[start]."""
    i = start + 1
    while i < len(s):
        if s[i] == "\\":
            i += 2
            continue
        if s[i] == '"':
            return i + 1
        i += 1
    raise ValueError("unterminated string: " + s)


def to_md(text):
    return text.replace('\\"', '"').replace("%%", "%")


def to_rpy(text):
    return text.replace("%", "%%").replace('"', '\\"')


def indent_of(line):
    return len(line) - len(line.lstrip(" "))


def git_commit():
    try:
        return subprocess.check_output(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
                                       text=True).strip()
    except Exception:
        return "unknown"


SAY_RE = re.compile(r'^(\s*)((?:[a-z_]\w*)(?: [a-z_]\w*)*)? ?(?=")')


def parse_say(line, chars):
    """Return (indent, who, attrs, text, suffix) for a say statement or menu
    caption/choice, or None."""
    m = SAY_RE.match(line)
    if not m:
        return None
    ind, head = m.group(1), m.group(2)
    who, attrs = None, []
    if head:
        words = head.split()
        if words[0] in STATEMENT_WORDS or words[0] not in chars:
            return None
        who, attrs = words[0], words[1:]
    q = m.end()
    end = string_end(line, q)
    return ind, who, attrs, line[q + 1:end - 1], line[end:]


# ---------------------------------------------------------------- export

def export(md_path, quiet=False):
    chars = load_characters()
    out = [
        "# Do Not Disturb: all dialogue",
        "",
        "<!-- exported from commit %s -->" % git_commit(),
        "",
        "Edit this file and send it back; the changes get applied to the game.",
        "",
        "- **Change a line:** edit the text after its tag (the `juni:42` at the start). "
        "Keep the tag.",
        "- **Change who speaks or their expression:** edit the bold name, e.g. "
        "`**Juni (happy):**`. Expressions are neutral, happy, surprised and blush. "
        "No bold name means narration.",
        "- **Add a line:** write it on a new line (no tag) under the line it should follow.",
        "- **Delete a line:** delete the whole line, tag included. Choices (lines with ▸) "
        "can be reworded but not deleted.",
        "- Lines starting with `>` are notes on what happens (scene changes, menus, "
        "rapport). They're for context and changes to them are ignored. Rapport is how much "
        "a choice raises (or lowers) that guest's affection; 10 unlocks their romance.",
        "- `{i}...{/i}` is italics in the game. `[name]` fills in a value while playing; "
        "leave those as they are.",
        "",
    ]
    for f in FILES:
        path = os.path.join(GAME, f + ".rpy")
        lines = open(path, encoding="utf-8").read().split("\n")
        out += ["", "---", "", "# %s.rpy" % f, ""]
        menu_stack = []      # indents of open menus
        choice_stack = []    # indents of open choices
        in_speed = False
        for n, raw in enumerate(lines, 1):
            line = raw.rstrip()
            st = line.strip()
            if not st or st.startswith("#"):
                continue
            ind = indent_of(line)
            while menu_stack and ind <= menu_stack[-1]:
                menu_stack.pop()
                out.append("> *(end of choice)*")
                out.append("")
            while choice_stack and ind <= choice_stack[-1]:
                choice_stack.pop()
            tag = "`%s:%d`" % (f, n)

            if st.startswith("SPEED_LINES"):
                in_speed = True
                out += ["", "> **Platonic Speed Dating: what each guest says when they're on your side**", ""]
                continue
            if in_speed:
                m = re.match(r'\s*\("(\w+)", (\d)\): \("(\w+)", "(\w+)", "', line)
                if m:
                    who, rnd, var, expr = m.groups()
                    q = line.index('"', m.end() - 1)
                    text = line[q + 1:string_end(line, q) - 1]
                    out.append("%s **%s (%s):** %s  " % (tag, chars[var], expr, to_md(text)))
                    if who == "zyx":
                        out.append("")
                    continue
                if st.startswith("}"):
                    in_speed = False
                continue
            m = re.match(r'\s*renpy\.say\(None, "', line)
            if m:
                q = m.end() - 1
                out.append("%s %s  " % (tag, to_md(line[q + 1:string_end(line, q) - 1])))
                continue

            if st.startswith("label "):
                out += ["", "## %s" % st[6:].rstrip(":"), ""]
                continue
            if st == "menu:" or re.match(r"menu\b.*:$", st):
                menu_stack.append(ind)
                out += ["", "> **Choice**"]
                continue
            if st.startswith(("scene ", "show ")) and not st.startswith(("show screen", "show text")):
                out.append("> *%s*  " % st.split(" with ")[0])
                continue
            if st.startswith(("jump ", "call ")):
                out.append("> *→ %s*  " % st)
                continue
            if re.match(r"(if|elif) .*:$", st) or st == "else:":
                out.append("> *%s*  " % st)
                continue
            m = re.match(r'\$ gain\("(\w+)", (-?\d+)\)', st)
            if m:
                amt = int(m.group(2))
                out.append("> *rapport %s%d %s*  " % ("+" if amt >= 0 else "−", abs(amt),
                                                       GUEST_NAMES.get(m.group(1), m.group(1))))
                continue
            if not st.startswith('"') and not re.match(r'[a-z_]\w*( [a-z_]\w*)* "', st):
                continue
            p = parse_say(line, chars)
            if not p:
                continue
            _, who, attrs, text, suffix = p
            is_choice = menu_stack and suffix.rstrip().endswith(":") and ind == menu_stack[-1] + 4
            if is_choice:
                depth = len(menu_stack)
                cond = re.search(r"\bif (.*):\s*$", suffix)
                out.append("")
                out.append("%s **%s** %s  " % (tag, "▸" * depth, to_md(text)))
                if cond:
                    out.append("> *(shown if %s)*  " % cond.group(1))
                choice_stack.append(ind)
                continue
            name = ""
            if who:
                name = "**%s%s:** " % (chars[who], " (%s)" % " ".join(attrs) if attrs else "")
            out.append("%s %s%s  " % (tag, name, to_md(text)))
        while menu_stack:
            menu_stack.pop()
            out.append("> *(end of choice)*")
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text) + "\n"
    open(md_path, "w", encoding="utf-8").write(text)
    if not quiet:
        print("wrote", os.path.relpath(md_path, ROOT))


# ---------------------------------------------------------------- import

TAG_RE = re.compile(r"^`(\w+):(\d+)`\s?(.*)$")


def parse_payload(payload, chars):
    """-> (kind, who, attrs, text). kind is 'choice' or 'say'."""
    payload = payload.rstrip()
    m = re.match(r"\*\*▸+\*\*\s?(.*)$", payload)
    if m:
        return "choice", None, [], m.group(1)
    m = re.match(r"\*\*(.+?):\*\*\s?(.*)$", payload)
    if m:
        label, text = m.groups()
        by_name = {v: k for k, v in chars.items()}
        for name in sorted(by_name, key=len, reverse=True):
            if label == name:
                return "say", by_name[name], [], text
            if label.startswith(name + " (") and label.endswith(")"):
                return "say", by_name[name], label[len(name) + 2:-1].split(), text
        raise SystemExit("Unknown speaker %r in: %s" % (label, payload))
    return "say", None, [], payload


def do_import(md_path):
    chars = load_characters()
    md = open(md_path, encoding="utf-8").read().split("\n")
    edits = {f: {} for f in FILES}      # line -> payload
    inserts = {f: {} for f in FILES}    # line -> [payloads]
    last = None
    for line in md:
        st = line.strip()
        m = TAG_RE.match(st)
        if m:
            f, n, payload = m.group(1), int(m.group(2)), m.group(3)
            if f not in edits:
                raise SystemExit("Unknown file in tag: " + st)
            edits[f][n] = payload
            last = (f, n)
            continue
        if not st or st.startswith((">", "#", "---", "<!--", "- ")) or last is None:
            if st.startswith("#"):
                last = None if st.startswith("# ") else last
            continue
        if st.startswith("Edit this file"):
            continue
        inserts[last[0]].setdefault(last[1], []).append(st)

    # Which lines are editable, according to a fresh export of the scripts?
    tmp = md_path + ".check"
    export(tmp, quiet=True)
    fresh_all = {f: {} for f in FILES}
    for l in open(tmp, encoding="utf-8"):
        m = TAG_RE.match(l.strip())
        if m:
            fresh_all[m.group(1)][int(m.group(2))] = m.group(3).rstrip()
    os.remove(tmp)

    changed = 0
    for f in FILES:
        path = os.path.join(GAME, f + ".rpy")
        lines = open(path, encoding="utf-8").read().split("\n")
        fresh = fresh_all[f]
        missing = set(edits[f]) - set(fresh)
        if missing:
            raise SystemExit("%s.rpy has changed since this file was exported (tags %s don't "
                             "match). Import on the exported commit instead." % (f, sorted(missing)[:5]))
        new = []
        for n, raw in enumerate(lines, 1):
            if n not in fresh:
                new.append(raw)
            elif n not in edits[f]:
                kind = "choice" if fresh[n].startswith("**▸") else "say"
                if kind == "choice" or "SPEED" in raw or "renpy.say" in raw:
                    print("note: kept %s:%d (choices and speed-dating lines can't be deleted)" % (f, n))
                    new.append(raw)
                else:
                    new.append(None)   # deleted
                    changed += 1
            else:
                payload = edits[f][n]
                if payload.rstrip() == fresh[n]:
                    new.append(raw)
                else:
                    new.append(rewrite(raw, payload, chars))
                    changed += 1
            for ins in inserts[f].get(n, []):
                kind, who, attrs, text = parse_payload(ins, chars)
                base = indent_of(raw) + (4 if raw.rstrip().endswith(":") else 0)
                head = (who + "".join(" " + a for a in attrs) + " ") if who else ""
                new.append(" " * base + head + '"%s"' % to_rpy(text))
                changed += 1
        # A block left empty by deletions gets a "pass".
        out = []
        for i, l in enumerate(new):
            if l is None:
                prev = next((x for x in reversed(out) if x.strip()), "")
                nxt = next((x for x in new[i + 1:] if x is not None and x.strip()), "")
                if prev.rstrip().endswith(":") and indent_of(nxt) <= indent_of(prev):
                    out.append(" " * (indent_of(prev) + 4) + "pass")
                continue
            out.append(l)
        if out != lines:
            open(path, "w", encoding="utf-8").write("\n".join(out))
            print("updated", f + ".rpy")
    print("%d change(s) applied" % changed)


def rewrite(raw, payload, chars):
    kind, who, attrs, text = parse_payload(payload, chars)
    m = re.match(r'(\s*\("\w+", \d\): \(")(\w+)", "(\w+)(", ")', raw)
    if m:
        q = m.end() - 1
        var = who or m.group(2)
        expr = attrs[0] if attrs else m.group(3)
        return m.group(1) + var + '", "' + expr + '", "%s"' % to_rpy(text) + raw[string_end(raw, q):]
    m = re.match(r'(\s*renpy\.say\(None, ")', raw)
    if m:
        q = m.end() - 1
        return raw[:q] + '"%s"' % to_rpy(text) + raw[string_end(raw, q):]
    ind, owho, oattrs, otext, suffix = parse_say(raw, chars)
    if kind == "choice":
        return ind + '"%s"' % to_rpy(text) + suffix
    head = (who + "".join(" " + a for a in attrs) + " ") if who else ""
    return ind + head + '"%s"' % to_rpy(text) + suffix


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "export"
    md = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_MD
    if cmd == "export":
        export(md)
    elif cmd == "import":
        do_import(md)
    else:
        raise SystemExit(__doc__)
