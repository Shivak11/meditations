"""Run with python3 -m unittest discover -s tests -p 'test_select_design.py'."""

import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "meditations"
SCRIPT = SKILL / "scripts" / "select_design.py"
spec = importlib.util.spec_from_file_location("select_design", SCRIPT)
selector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(selector)


def contrast(first, second):
    def luminance(hex_colour):
        values = [int(hex_colour[index:index + 2], 16) / 255 for index in (1, 3, 5)]
        linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
                  for value in values]
        return sum(a * b for a, b in zip(linear, (0.2126, 0.7152, 0.0722)))
    low, high = sorted((luminance(first), luminance(second)))
    return (high + 0.05) / (low + 0.05)


class SelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.systems = selector.load_registry()
        cls.ids = {item["id"] for item in cls.systems}

    def test_default_uses_system_random_and_no_seed(self):
        with mock.patch.object(selector.random, "SystemRandom") as system_random:
            with mock.patch.object(selector.random, "Random") as seeded_random:
                system_random.return_value.choice.side_effect = lambda options: options[-1]
                selected = selector.select_design(self.systems)
        system_random.assert_called_once_with()
        seeded_random.assert_not_called()
        self.assertEqual(selected["id"], self.systems[-1]["id"])
        self.assertEqual(selected["selection_method"], "system-random")

    def test_seeded_runs_repeat_and_can_reach_every_system(self):
        for seed in (0, 1, -7, 1048576):
            first = selector.select_design(self.systems, seed=seed)
            self.assertEqual(first, selector.select_design(self.systems, seed=seed))
            self.assertEqual(first["selection_method"], "seeded")
        picks = {selector.select_design(self.systems, seed=seed)["id"] for seed in range(100)}
        self.assertEqual(picks, self.ids)

    def test_kind_and_exclusions_bound_the_pool(self):
        for kind in selector.KINDS:
            eligible = [item["id"] for item in self.systems if kind in item["kinds"]]
            exclusions = eligible[:2]
            remaining = set(eligible) - set(exclusions)
            self.assertTrue(remaining)
            for seed in range(30):
                result = selector.select_design(self.systems, seed=seed, kind=kind,
                                                exclude=exclusions)
                self.assertIn(result["id"], remaining)
                self.assertFalse(result["exclusions_reset"])

    def test_all_excluded_recovers_within_requested_kind(self):
        eligible = [item["id"] for item in self.systems if "process" in item["kinds"]]
        self.assertEqual(len(eligible), 3)
        for seed in range(20):
            result = selector.select_design(self.systems, seed=seed, kind="process",
                                            exclude=eligible)
            self.assertIn(result["id"], eligible)
            self.assertTrue(result["exclusions_reset"])
            self.assertEqual(result["kind"], "process")

    def test_empty_and_stale_history_are_safe(self):
        empty = selector.select_design(self.systems, seed=9)
        stale = selector.select_design(self.systems, seed=9, exclude=["retired-design"])
        self.assertEqual(empty["id"], stale["id"])
        self.assertEqual(empty["excluded_ids"], [])
        self.assertEqual(stale["ignored_exclusions"], ["retired-design"])
        self.assertFalse(stale["exclusions_reset"])

    def test_duplicate_exclusions_do_not_reduce_pool_twice(self):
        result = selector.select_design(self.systems, seed=7,
                                        exclude=["paper-notes", "paper-notes"])
        self.assertNotEqual(result["id"], "paper-notes")
        self.assertEqual(result["excluded_ids"], ["paper-notes"])

    def test_invalid_inputs_fail_clearly(self):
        with self.assertRaisesRegex(ValueError, "at most three"):
            selector.select_design(self.systems, exclude=list(self.ids)[:4])
        with self.assertRaisesRegex(ValueError, "Unknown study kind"):
            selector.select_design(self.systems, kind="unsupported")
        with self.assertRaisesRegex(ValueError, "No design systems"):
            selector.select_design([])
        subset = [item for item in self.systems if "process" not in item["kinds"]]
        with self.assertRaisesRegex(ValueError, "No design systems support"):
            selector.select_design(subset, kind="process")

    def test_cli_is_cwd_independent_json_and_does_not_write(self):
        def snapshot():
            return {str(path.relative_to(SKILL)): hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in SKILL.rglob("*") if path.is_file()}
        before = snapshot()
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, str(SCRIPT), "--seed", "42"],
                                    cwd=directory, text=True, capture_output=True, check=True)
            self.assertEqual(list(Path(directory).iterdir()), [])
        data = json.loads(result.stdout)
        self.assertEqual(result.stderr, "")
        self.assertIn(data["id"], self.ids)
        self.assertTrue((SKILL / data["css"]).is_file())
        self.assertFalse(Path(data["css"]).is_absolute())
        self.assertEqual(before, snapshot())

    def test_cli_errors_emit_no_fake_selection(self):
        for args in (["--kind", "unsupported"], ["--seed", "not-a-number"],
                     ["--exclude", "a", "--exclude", "b", "--exclude", "c", "--exclude", "d"]):
            result = subprocess.run([sys.executable, str(SCRIPT), *args],
                                    text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")
            self.assertTrue(result.stderr.strip())


class CatalogueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.systems = selector.load_registry()

    def test_five_distinct_complete_systems(self):
        self.assertEqual(len(self.systems), 5)
        folder = SKILL / "assets" / "design-systems"
        self.assertEqual({path.name for path in folder.glob("*.css")},
                         {item["id"] + ".css" for item in self.systems})
        for field in ("id", "name", "brief", "css", "typography", "layout", "diagram"):
            self.assertEqual(len({item[field] for item in self.systems}), 5, field)

    def test_bundle_uses_no_external_assets_or_imports(self):
        for item in self.systems:
            css = (SKILL / item["css"]).read_text()
            self.assertNotRegex(css.lower(), r"@import|@font-face|url\s*\(|https?://")
            self.assertNotIn("/Users/", css)
        tree = ast.parse(SCRIPT.read_text())
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module.split(".")[0])
        self.assertLessEqual(imports, {"argparse", "json", "pathlib", "random", "re", "sys"})

    def test_text_and_control_contrast(self):
        for item in self.systems:
            css = (SKILL / item["css"]).read_text()
            root = re.search(r":root\s*\{(.*?)\}", css, re.S).group(1)
            tokens = dict(re.findall(r"(--[\w-]+):\s*(#[0-9a-fA-F]{6})\s*;", root))
            for pairs, minimum in (("text_contrast_pairs", 4.5),
                                   ("nontext_contrast_pairs", 3.0)):
                self.assertGreaterEqual(len(item[pairs]), 5)
                for foreground, background in item[pairs]:
                    first = tokens[foreground] if foreground.startswith("--") else foreground
                    second = tokens[background] if background.startswith("--") else background
                    with self.subTest(design=item["id"], pair=(foreground, background)):
                        self.assertGreaterEqual(contrast(first, second), minimum)

    def test_accessibility_defaults_are_present_in_every_standalone_css(self):
        for item in self.systems:
            css = (SKILL / item["css"]).read_text()
            with self.subTest(design=item["id"]):
                self.assertRegex(css, r"--body-size:\s*20px")
                self.assertRegex(css, r"--small-size:\s*18px")
                self.assertRegex(css, r"body\s*\{[^}]*font:\s*var\(--body-size\)")
                self.assertRegex(css, r"min-height:\s*44px")
                self.assertIn(":focus-visible", css)
                self.assertIn("@media (max-width: 700px)", css)
                self.assertIn("@media (prefers-reduced-motion: reduce)", css)
                self.assertIn("@media print", css)
                self.assertIn("details::details-content", css)
                self.assertNotIn("font-style: italic", css)

    def test_registry_rejects_duplicate_missing_empty_and_escaping_assets(self):
        catalogue = json.loads(selector.REGISTRY.read_text())
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            registry = folder / "registry.json"
            for item in catalogue["systems"]:
                (folder / (item["id"] + ".css")).write_text("body { font-size: 20px; }")
            def check(changed, message):
                registry.write_text(json.dumps(changed))
                with self.assertRaisesRegex(ValueError, message):
                    selector.load_registry(registry)
            changed = json.loads(json.dumps(catalogue))
            changed["systems"].append(changed["systems"][0])
            check(changed, "Duplicate")
            changed = json.loads(json.dumps(catalogue))
            changed["systems"][0]["css"] = "../../outside.css"
            check(changed, "CSS path")
            changed = json.loads(json.dumps(catalogue))
            changed["systems"][0]["kinds"] = ["unsupported"]
            check(changed, "study kinds")
            css = folder / (catalogue["systems"][0]["id"] + ".css")
            css.write_text("")
            check(catalogue, "empty")
            css.unlink()
            check(catalogue, "missing")


if __name__ == "__main__":
    unittest.main()
