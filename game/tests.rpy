## tests.rpy — an automated player that runs through the whole game.
##
## Does nothing during normal play. It switches on only when the game is
## started with the environment variable VN_TEST=1, e.g.
##
##     VN_TEST=1 VN_TEST_REPORT=report.txt RENPY_PERFORMANCE_TEST=0 \
##         renpy.sh /path/to/visualnovel
##
## In test mode the game skips the main menu, fast-skips all dialogue, and
## makes every menu choice itself. It plays these cases:
##
##   full-<guest>-<n>   The whole game, following <guest> in every pool and
##                      hallway menu, picking option n (0, 1, 2) in every
##                      conversation menu. 5 guests x 3 = 15 runs.
##   wanderer           The whole game, wandering alone every night.
##   ending-*           Straight to the finale with rapport set up to reach
##                      every ending, including several guests qualifying.
##   screens            Opens the Guest Book with and without guests met.
##
## Every exception is caught and recorded instead of stopping the game.
## At the end it writes a report (VN_TEST_REPORT, default vn_test_report.txt
## in the project folder) listing failures, labels never reached and menu
## options never chosen, then quits with status 1 if anything failed.

init -100 python:
    import os as _vn_os
    vn_testing = bool(_vn_os.environ.get("VN_TEST"))

init python:
    import os, time, traceback, json

    VN_EXPECTED_ROMANCE = {
        "juni": "Regeneration", "gerald": "Not Blurry", "solstice": "The Longest Day",
        "wren": "Off Duty", "zyx": "First Contact",
    }

    def vn_build_cases():
        cases = []
        for g in GUESTS:
            for k in (0, 1, 2):
                cases.append({"name": "full-%s-%d" % (g, k), "kind": "full", "target": g, "option": k})
        cases.append({"name": "wanderer", "kind": "full", "target": "wander", "option": 0})
        for g in GUESTS:
            cases.append({"name": "ending-romance-" + g, "kind": "finale", "rapport": {g: ROMANCE_THRESHOLD},
                          "target": g, "expect": VN_EXPECTED_ROMANCE[g]})
            cases.append({"name": "ending-friend-" + g, "kind": "finale", "rapport": {g: FRIEND_THRESHOLD},
                          "target": g, "expect": "Good Company", "expect_friend": g})
        cases.append({"name": "ending-several-qualify-choose-alone", "kind": "finale",
                      "rapport": {g: ROMANCE_THRESHOLD for g in GUESTS}, "target": "alone",
                      "expect": "Good Company"})
        cases.append({"name": "ending-checkout", "kind": "finale", "rapport": {}, "target": "alone",
                      "expect": "Checkout"})
        return cases

    class VNTest(object):
        def __init__(self):
            self.cases = vn_build_cases()
            self.index = 0
            self.case = None
            self.failures = []          # (case, message)
            self.labels_seen = set()
            self.menus = {}             # (file, line) -> [n_options, set(chosen indexes), sample caption]
            self.started = time.time()
            self.case_started = 0
            self.results = []           # (case, ending, seconds)
            self.interactions = 0
            self.no_skip = False

        def fail(self, msg):
            name = self.case["name"] if self.case else "setup"
            self.failures.append((name, msg))
            if len(self.failures) > 200:
                self.write_report()
                renpy.quit(status=1)

    vn = VNTest() if vn_testing else None

    def vn_reset_state(case):
        store.rapport = {g: 0 for g in GUESTS}
        store.pool_seen = {g: 0 for g in GUESTS}
        store.night_seen = {g: 0 for g in GUESTS}
        store.met = set()
        store.day = 1
        store.met_tonight = []
        store.wanders = 0
        store.chosen = None
        store.who = None
        store.ending_name = ""
        store.candidates = []
        store.friend = None
        store.time_label = ""
        for g, v in case.get("rapport", {}).items():
            store.rapport[g] = v
            store.met.add(g)
        if case["kind"] == "finale":
            store.day = 4

    def vn_begin_case():
        vn.case = vn.cases[vn.index]
        vn.case_started = time.time()
        vn.interactions = 0
        vn_reset_state(vn.case)

    def vn_end_case():
        case = vn.case
        ending = store.ending_name
        vn.results.append((case["name"], ending, time.time() - vn.case_started))
        if not ending:
            vn.fail("never reached an ending card")
        if case.get("expect") and ending != case["expect"]:
            vn.fail("expected ending %r, got %r" % (case["expect"], ending))
        if case.get("expect_friend") and store.friend != case["expect_friend"]:
            vn.fail("expected friend ending with %r, got %r" % (case["expect_friend"], store.friend))
        if case["kind"] == "full" and case["target"] in GUESTS:
            g = case["target"]
            if store.pool_seen[g] != 2 or store.night_seen[g] != 3:
                vn.fail("following %s should see 2 pool + 3 night chapters, saw %d + %d"
                        % (g, store.pool_seen[g], store.night_seen[g]))
        if case["name"] == "wanderer" and store.wanders != 6:
            vn.fail("wanderer should wander 6 times, wandered %d" % store.wanders)
        vn.index += 1

    def vn_menu(items):
        """Replaces the normal choice menu while testing."""
        choices = [(label, value) for (label, value) in items if value is not None]
        where = renpy.get_filename_line()
        rec = vn.menus.setdefault(where, [len(choices), set(), choices[0][0] if choices else ""])
        rec[0] = max(rec[0], len(choices))

        tags = [(getattr(v, "kwargs", None) or {}).get("guest") for (l, v) in choices]
        target = vn.case["target"]

        if any(tags):
            # A routing menu (pool / hallway / finale): steer toward the target.
            if target in tags:
                idx = tags.index(target)
            else:
                # Otherwise pick the first guest on offer (not wandering, not alone).
                idx = next((i for i, t in enumerate(tags) if t not in ("wander", "alone")), 0)
        else:
            idx = min(vn.case.get("option", 0), len(choices) - 1)

        rec[1].add(idx)
        value = choices[idx][1]
        return value.value if hasattr(value, "value") else value

    def vn_label_callback(name, abnormal):
        vn.labels_seen.add(name)

    def vn_interact():
        vn.interactions += 1
        if vn.interactions > 20000:
            vn.fail("too many interactions; is the game stuck in a loop?")
            vn.write_report()
            renpy.quit(status=1)
        if not vn.no_skip:
            renpy.config.skipping = "fast"

    def vn_exception(*args):
        # Ren'Py passes either (short, full, traceback_fn) or one TracebackException.
        if len(args) == 1:
            te = args[0]
            text = "".join(getattr(te, "format", lambda: [str(te)])())
        else:
            text = args[1] if len(args) > 1 else str(args)
        lines = [l for l in text.strip().splitlines() if l.strip()]
        vn.fail("EXCEPTION: " + "\n      ".join(lines[-12:]))
        return True  # handled: carry on with the next statement

    def vn_check_screens():
        """Render the Guest Book for a moment in two states."""
        vn.no_skip = True
        renpy.config.skipping = None
        try:
            for met_set in (set(), set(GUESTS)):
                store.met = met_set
                renpy.show_screen("guest_book")
                renpy.pause(0.2, hard=True)
                renpy.hide_screen("guest_book")
            store.time_label = "Test — Time Tag"
            renpy.pause(0.1, hard=True)
        finally:
            vn.no_skip = False
            store.met = set()

    def write_report():
        out = os.environ.get("VN_TEST_REPORT") or os.path.join(config.basedir, "vn_test_report.txt")
        all_labels = sorted(l for l in renpy.get_all_labels()
                            if isinstance(l, str) and not l.startswith("_") and "." not in l
                            and l not in ("splashscreen", "main_menu", "after_load", "quit", "vn_test_main"))
        unreached = [l for l in all_labels if l not in vn.labels_seen]
        partial = []
        for (fn, line), (n, chosen, caption) in sorted(vn.menus.items()):
            if len(chosen) < n:
                partial.append("%s:%d  took %s of %d options  (first option: %s)"
                               % (fn, line, sorted(chosen), n, caption[:60]))

        lines = []
        status = "FAIL" if (vn.failures or unreached) else "PASS"
        lines.append("Do Not Disturb — automated playthrough report: %s" % status)
        lines.append("Cases run: %d   Failures: %d   Labels unreached: %d   Menus not fully covered: %d   Time: %.1fs"
                     % (len(vn.results), len(vn.failures), len(unreached), len(partial), time.time() - vn.started))
        lines.append("")
        lines.append("FAILURES")
        for case, msg in vn.failures:
            lines.append("  [%s] %s" % (case, msg))
        if not vn.failures:
            lines.append("  none")
        lines.append("")
        lines.append("LABELS NEVER REACHED")
        lines.extend("  " + l for l in unreached) if unreached else lines.append("  none")
        lines.append("")
        lines.append("MENUS WHERE SOME OPTIONS WERE NEVER CHOSEN (informational)")
        lines.extend("  " + p for p in partial) if partial else lines.append("  none")
        lines.append("")
        lines.append("CASES")
        for name, ending, secs in vn.results:
            lines.append("  %-40s ending=%-18s %.1fs" % (name, ending or "-", secs))
        with open(out, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print("\n".join(lines))
        return status

    VNTest.write_report = lambda self: write_report()

    if vn_testing:
        if hasattr(config, "label_callbacks"):      # Ren'Py 8.4+
            config.label_callbacks.append(vn_label_callback)
        else:
            config.label_callback = vn_label_callback
        config.interact_callbacks.append(vn_interact)
        config.exception_handler = vn_exception
        config.fast_skipping = True
        config.allow_skipping = True
        config.skip_delay = 0
        menu = vn_menu


## In test mode, skip the main menu and run the suite.
label splashscreen:
    if vn_testing:
        $ _preferences.skip_unseen = True
        $ _preferences.skip_after_choices = True
        jump vn_test_main
    return


label vn_test_main:
    $ vn_check_screens()

    while vn.index < len(vn.cases):
        $ vn_begin_case()
        if vn.case["kind"] == "full":
            call start
        else:
            call finale
        $ vn_end_case()

    python:
        _vn_status = write_report()
        renpy.quit(status=1 if _vn_status == "FAIL" else 0)
    return
