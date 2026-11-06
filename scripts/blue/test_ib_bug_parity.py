#!/usr/bin/env python3
"""Tests for ib_bug_parity.py, ib_media_fix.sh and ib_extract_program_id.py. Offline. Run: python3 test_ib_bug_parity.py -v
Fixtures: /workspace/ib-bug-parity-fixtures/ (override with IB_PARITY_FIXTURES)."""
import os, shutil, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "ib_bug_parity.py")
FIXER = os.path.join(HERE, "ib_media_fix.sh")
EXTRACT = os.path.join(HERE, "ib_extract_program_id.py")
FX = os.environ.get("IB_PARITY_FIXTURES", "/workspace/ib-bug-parity-fixtures")


def run(*args):
    a = []
    for x in args:
        a.append(os.path.join(FX, x) if x.endswith((".jsonl", ".json")) else x)
    p = subprocess.run([sys.executable, SCRIPT, *a], capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def kinds(out):
    return sorted(l.split()[0] for l in out.splitlines()
                  if l and l.split()[0] not in ("OK", "SUMMARY") and not l.endswith("problem(s)"))


class Parity(unittest.TestCase):
    def test_all_good(self):
        rc, out, _ = run("--ledger", "good.jsonl", "--source-bugs", "source_good.json",
                         "--cards-export", "cards_good.json", "--bugs-export", "bugs_good.json")
        self.assertEqual(rc, 0, out)
        self.assertIn("OK 3/3 bugs have card + #bugs post, media attached 10/10", out)

    def test_missing_bugs_post_todays_failure(self):
        rc, out, _ = run("--ledger", "missing_bugs_post.jsonl")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["MISSING_BUGS_POST"], out)
        self.assertIn("1792603801.673819", out)

    def test_missing_card(self):
        rc, out, _ = run("--ledger", "missing_card.jsonl")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["MISSING_CARD"], out)

    def test_media_short(self):
        rc, out, _ = run("--ledger", "media_short.jsonl")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["MEDIA_SHORT"], out)
        self.assertIn("card has 1, expected exactly 2", out)

    def test_media_extra_is_not_a_pass(self):
        rc, out, _ = run("--ledger", "media_extra.jsonl")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["MEDIA_EXTRA"], out)

    def test_corrupt_video_with_permalink_fails(self):
        # Ryne 2026-10-22: a permalink no longer counts; media must be attached
        rc, out, _ = run("--ledger", "corrupt_video_permalink.jsonl")
        self.assertEqual(rc, 1, out)
        self.assertEqual(kinds(out), ["MEDIA_NOT_ATTACHED", "MEDIA_SHORT", "MEDIA_SHORT"], out)
        self.assertNotIn("MISSING_PERMALINK", out)

    def test_corrupt_video_without_permalink(self):
        rc, out, _ = run("--ledger", "corrupt_video_no_permalink.jsonl")
        self.assertEqual(rc, 1)
        self.assertIn("MEDIA_NOT_ATTACHED", out)
        self.assertIn("MISSING_PERMALINK", out)

    def test_corrupt_video_fixed_and_attached_passes(self):
        rc, out, _ = run("--ledger", "corrupt_video_fixed.jsonl")
        self.assertEqual(rc, 0, out)
        self.assertIn("OK 1/1", out)

    def test_duplicate(self):
        rc, out, _ = run("--ledger", "duplicate.jsonl")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["DUPLICATE"], out)

    def test_missing_ledger(self):
        rc, out, _ = run("--ledger", "good.jsonl", "--source-bugs", "source_extra.json")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["MISSING_LEDGER"], out)
        self.assertIn("1792690000.000004", out)

    def test_card_not_found_and_export_media(self):
        rc, out, _ = run("--ledger", "good.jsonl", "--cards-export", "cards_missing_one.json")
        self.assertEqual(rc, 1)
        # card ...002 missing; card ...001 export shows 1 attachment, ledger claims 2
        self.assertEqual(kinds(out), ["CARD_NOT_FOUND", "MEDIA_SHORT"], out)

    def test_bugs_post_must_be_top_level(self):
        rc, out, _ = run("--ledger", "good.jsonl", "--bugs-export", "bugs_reply_only.json")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["BUGS_POST_NOT_FOUND"], out)

    def test_since_filters_old_rows(self):
        rc, out, _ = run("--ledger", "old_and_new.jsonl", "--since", "2026-10-21")
        self.assertEqual(rc, 0, out)
        rc, out, _ = run("--ledger", "old_and_new.jsonl")
        self.assertEqual(rc, 1)

    def test_empty_ledger_ok(self):
        rc, out, _ = run("--ledger", "empty.jsonl")
        self.assertEqual(rc, 0)
        self.assertIn("OK 0/0", out)

    def test_malformed_inputs_exit_2(self):
        for f in ("malformed_json.jsonl", "malformed_missing_field.jsonl",
                  "malformed_bad_count.jsonl", "malformed_bad_ts.jsonl", "nope.jsonl"):
            rc, out, err = run("--ledger", f)
            self.assertEqual(rc, 2, f"{f}: {out}{err}")
            self.assertIn("bad input", err)
        rc, _, _ = run("--ledger", "good.jsonl", "--bugs-export", "bad_export.json")
        self.assertEqual(rc, 2)
        rc, _, _ = run("--ledger", "good.jsonl", "--since", "10/21")
        self.assertEqual(rc, 2)

    # ---- program ID (Ryne 2026-10-22: always pull the program ID) ----
    def test_program_id_missing(self):
        rc, out, _ = run("--ledger", "program_id_missing.jsonl")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["MISSING_PROGRAM_ID"], out)

    def test_program_id_not_hex24(self):
        rc, out, _ = run("--ledger", "program_id_bad_hex.jsonl")
        self.assertEqual(rc, 1)
        self.assertIn("is not 24-char hex", out)

    def test_asked_ryne_needs_asked_at(self):
        rc, out, _ = run("--ledger", "program_id_asked_no_time.jsonl")
        self.assertEqual(rc, 1)
        self.assertIn("asked_ryne needs asked_at", out)

    def test_asked_ryne_with_asked_at_passes(self):
        rc, out, _ = run("--ledger", "program_id_asked_ok.jsonl")
        self.assertEqual(rc, 0, out)

    def test_waiting_on_ryne_still_fails(self):
        rc, out, _ = run("--ledger", "program_id_waiting_on_ryne.jsonl")
        self.assertEqual(rc, 1)
        self.assertIn("waiting on Ryne since 2026-10-22 07:10 CT", out)

    def test_program_id_from_image_passes(self):
        self.assertEqual(run("--ledger", "program_id_from_image.jsonl")[0], 0)

    def test_program_related_unset(self):
        rc, out, _ = run("--ledger", "program_related_unset.jsonl")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["PROGRAM_RELATED_UNSET"], out)

    def test_program_related_not_bool_is_bad_input(self):
        self.assertEqual(run("--ledger", "malformed_program_related.jsonl")[0], 2)

    def test_program_id_line_required_in_post(self):
        rc, out, _ = run("--ledger", "program_id_from_image.jsonl", "--bugs-export", "bugs_no_program_line.json")
        self.assertEqual(rc, 1)
        self.assertEqual(kinds(out), ["PROGRAM_ID_NOT_IN_POST"], out)

    def test_usage(self):
        self.assertEqual(run()[0], 2)
        rc, out, _ = run("--help")
        self.assertEqual(rc, 0)
        self.assertIn("--ledger", out)


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg not installed")
class MediaFix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = tempfile.mkdtemp(prefix="ibmf-")
        ff = lambda *a: subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)
        cls.mov = os.path.join(cls.d, "Screen Recording.mov")
        ff("-f", "lavfi", "-i", "testsrc2=size=1920x1080:rate=30", "-f", "lavfi", "-i", "sine=frequency=440",
           "-t", "15", "-c:v", "libx264", "-b:v", "8M", "-c:a", "aac", cls.mov)
        cls.small = os.path.join(cls.d, "small.mp4")
        ff("-f", "lavfi", "-i", "testsrc=size=640x360:rate=24", "-t", "3", "-c:v", "libx264", cls.small)
        cls.png = os.path.join(cls.d, "shot.png")
        ff("-f", "lavfi", "-i", "testsrc=size=320x240", "-frames:v", "1", cls.png)
        cls.bad = os.path.join(cls.d, "corrupt.mov")
        with open(cls.mov, "rb") as s, open(cls.bad, "wb") as t:
            t.write(s.read(200000))
        cls.fake = os.path.join(cls.d, "fake.png")
        with open(cls.fake, "w") as fh:
            fh.write("not an image")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.d, ignore_errors=True)

    def fix(self, f):
        p = subprocess.run(["bash", FIXER, f, os.path.join(self.d, "out")], capture_output=True, text=True)
        return p.returncode, p.stdout, p.stderr

    def test_mov_over_10mb_transcoded(self):
        self.assertGreater(os.path.getsize(self.mov), 10_000_000)
        rc, out, err = self.fix(self.mov)
        self.assertEqual(rc, 0, err)
        path = out.strip().splitlines()[-1].split(" ", 1)[1]
        self.assertTrue(path.endswith(".mp4"))
        self.assertLess(os.path.getsize(path), 10_000_000)
        probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                "stream=codec_name,height", "-of", "csv=p=0", path], capture_output=True, text=True).stdout
        self.assertEqual(probe.strip(), "h264,720")

    def test_small_mp4_untouched(self):
        rc, out, _ = self.fix(self.small)
        self.assertEqual(rc, 0)
        self.assertTrue(out.strip().endswith(self.small))

    def test_corrupt_video_exit_3(self):
        rc, _, err = self.fix(self.bad)
        self.assertEqual(rc, 3)
        self.assertIn("CORRUPT video", err)

    def test_images(self):
        self.assertEqual(self.fix(self.png)[0], 0)
        self.assertEqual(self.fix(self.fake)[0], 3)

    def test_missing_file_exit_2(self):
        self.assertEqual(self.fix(os.path.join(self.d, "nope.mov"))[0], 2)


TESS = shutil.which("tesseract") or ("/home/box/.local/bin/tesseract" if os.path.exists("/home/box/.local/bin/tesseract") else None)


def extract(*args):
    p = subprocess.run([sys.executable, EXTRACT, *args], capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


class ExtractProgramId(unittest.TestCase):
    def test_url_and_text(self):
        rc, out, _ = extract("--text", "pdf broke <https://app.iron-blueprint.com/programs/view/6ad8f20fe2a7801835f5b603|link> "
                                       "and program 6ad000bd76ebc30affee04bb too")
        self.assertEqual(rc, 0)
        self.assertEqual(out.split("\n")[:2], ["6ad8f20fe2a7801835f5b603 url", "6ad000bd76ebc30affee04bb text"])

    def test_not_found_exit_4(self):
        rc, _, err = extract("--text", "search returns junk for paused, 3x15 sets")
        self.assertEqual(rc, 4)
        self.assertIn("NO_PROGRAM_ID", err)

    def test_25_hex_is_not_an_id(self):
        self.assertEqual(extract("--text", "6ad8f20fe2a7801835f5b6031")[0], 4)

    def test_ocr_swaps_only_when_valid(self):
        sys.path.insert(0, HERE)
        import ib_extract_program_id as x
        self.assertEqual(x.fix_ocr("6ad8f2Ofe2a78Ol835f5b6O3"), "6ad8f20fe2a7801835f5b603")
        self.assertEqual(x.fix_ocr("6adIf2lfe2a7801835f5b603"), "6ad1f21fe2a7801835f5b603")
        self.assertIsNone(x.fix_ocr("6ad8f2Xfe2a7801835f5b603"))
        self.assertFalse(x.plausible("62d8120fe237801835150603"))   # 2022 timestamp: OCR garbage
        self.assertTrue(x.plausible("6ad8f20fe2a7801835f5b603"))

    def test_missing_image_exit_2(self):
        self.assertEqual(extract("/nope/missing.png")[0], 2)

    @unittest.skipUnless(TESS, "tesseract not installed")
    def test_ocr_generated_image(self):
        from PIL import Image, ImageDraw, ImageFont
        d = tempfile.mkdtemp(prefix="ibpid-")
        try:
            path = os.path.join(d, "shot.png")
            im = Image.new("RGB", (900, 200), "white"); dr = ImageDraw.Draw(im)
            try:
                f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
            except OSError:
                f = ImageFont.load_default()
            dr.text((20, 30), "app.iron-blueprint.com/programs/view/6ad0dc9476ebc30afff85e66", fill="black", font=f)
            dr.text((20, 90), "Program: 5 week Strength   Coach: Ryne", fill="gray", font=f)
            im.save(path)
            rc, out, err = extract(path)
            self.assertEqual(rc, 0, err)
            self.assertEqual(out.strip(), "6ad0dc9476ebc30afff85e66 image:shot.png")
        finally:
            shutil.rmtree(d, ignore_errors=True)

    @unittest.skipUnless(TESS and os.path.exists(os.path.join(FX, "pdf_enoent_fullres_sim.png")), "fixture/tesseract missing")
    def test_full_size_address_bar_confirmed(self):
        rc, out, _ = extract(os.path.join(FX, "pdf_enoent_fullres_sim.png"))
        self.assertEqual((rc, out.strip()), (0, "6ad8f20fe2a7801835f5b603 image:pdf_enoent_fullres_sim.png"))

    @unittest.skipUnless(TESS and os.path.exists(os.path.join(FX, "pdf_enoent_fullres_sim.png")), "fixture/tesseract missing")
    def test_prefers_full_size_copy(self):
        rc, out, err = extract(os.path.join(FX, "pdf_enoent_fullres_sim-1024.png"), os.path.join(FX, "pdf_enoent_fullres_sim.png"))
        self.assertEqual(rc, 0)
        self.assertIn("SKIPPED pdf_enoent_fullres_sim-1024.png", err)
        self.assertEqual(out.strip(), "6ad8f20fe2a7801835f5b603 image:pdf_enoent_fullres_sim.png")

    @unittest.skipUnless(TESS and os.path.exists(os.path.join(FX, "pdf_enoent_slack_1024.png")), "fixture/tesseract missing")
    def test_slack_1024_preview_never_guesses(self):
        # the real 1024x576 Slack copy: OCR reads disagree, so no ID is reported (a wrong ID is worse than none)
        rc, out, err = extract(os.path.join(FX, "pdf_enoent_slack_1024.png"))
        self.assertEqual(rc, 4, out)
        self.assertEqual(out.strip(), "")
        self.assertIn("LOW_RES pdf_enoent_slack_1024.png is 1024x576", err)

    @unittest.skipUnless(TESS and os.path.exists(os.path.join(FX, "program_id_sample.png")), "fixture/tesseract missing")
    def test_ocr_fixture_image(self):
        rc, out, _ = extract(os.path.join(FX, "program_id_sample.png"))
        self.assertEqual((rc, out.strip()), (0, "6ad0dc9476ebc30afff85e66 image:program_id_sample.png"))


if __name__ == "__main__":
    unittest.main()
