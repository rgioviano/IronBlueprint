#!/usr/bin/env python3
"""Tests for ib_coach_test_lint.py. Fixtures in /workspace/ib-coach-test-fixtures/."""
import os, subprocess, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "ib_coach_test_lint.py")
F = "/workspace/ib-coach-test-fixtures"

def run(*args):
    p = subprocess.run([sys.executable, SCRIPT, *args], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr

class T(unittest.TestCase):
    def bad(self, fx, code):
        rc, out = run(os.path.join(F, fx))
        self.assertEqual(rc, 1, out); self.assertIn(code, out)
        return out
    def test_good(self):
        rc, out = run(f"{F}/good.md")
        self.assertEqual(rc, 0, out); self.assertIn("OK coach test post: 2 ready, 1 coming soon", out)
    def test_time_not_emoji(self):
        self.assertNotIn("EMOJI", run(f"{F}/good.md")[1])
    def test_none_this_time(self):
        rc, out = run(f"{F}/none_this_time.md")
        self.assertEqual(rc, 0, out); self.assertIn("2 ready, 0 coming soon", out)
    def test_no_channel(self): self.bad("no_channel.md", "NO_CHANNEL_TAG")
    def test_missing_section(self): self.bad("missing_section.md", "MISSING_SECTION")
    def test_wrong_order(self): self.assertIn("before", self.bad("wrong_order.md", "MISSING_SECTION"))
    def test_empty(self): self.bad("empty_section.md", "EMPTY_SECTION")
    def test_no_pass(self): self.bad("no_pass.md", "NO_PASS_CRITERIA")
    def test_emoji(self): self.assertEqual(self.bad("emoji.md", "EMOJI").count("EMOJI"), 1)
    def test_em_dash(self): self.bad("em_dash.md", "EM_DASH")
    def test_dev(self): self.bad("dev_name.md", "DEV_NAME")
    def test_basecamp(self): self.bad("basecamp.md", "BASECAMP_LINK")
    def test_secret(self):
        out = self.bad("secret.md", "SECRET_LIKE")
        self.assertEqual(out.count("SECRET_LIKE"), 4, out)
        self.assertNotIn("abcdef1234", out); self.assertNotIn("6ad8f20f", out)
    def test_no_closing(self): self.bad("no_closing.md", "NO_CLOSING")
    def test_closing_missing_program_id(self): self.bad("no_program_id.md", "NO_CLOSING")
    def test_approved_match(self):
        rc, out = run(f"{F}/good.md", "--approved", f"{F}/approved.md"); self.assertEqual(rc, 0, out)
    def test_approved_mismatch(self):
        rc, out = run(f"{F}/changed.md", "--approved", f"{F}/approved.md")
        self.assertEqual(rc, 1, out); self.assertIn("CHANGED_SINCE_APPROVAL line 4", out); self.assertIn("+- PDF viewer", out)
    def test_bad_input(self):
        self.assertEqual(run(f"{F}/nope.md")[0], 2)
    def test_help(self):
        rc, out = run("--help"); self.assertEqual(rc, 0); self.assertIn("--approved", out)

if __name__ == "__main__":
    unittest.main()
