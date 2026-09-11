import importlib.util
import io
from pathlib import Path
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package_skill", ROOT / "scripts/package_skill.py")
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


class PackageTests(unittest.TestCase):
    def test_allowlist_has_no_private_or_maintenance_files(self):
        sources = package.read_sources()
        for name, contents in sources.items():
            self.assertTrue(name.startswith("meditations/"))
            self.assertNotIn("..", Path(name).parts)
            self.assertFalse(any(part in name for part in ["evals/", "tests/", "plans/", "hooks/", "meditation.html"]))
            self.assertNotRegex(contents, rb"/(?:Users|home)/[^/\s]+/")
            self.assertNotRegex(contents, rb"\.(?:claude|codex)/settings[^/\s]*")
        self.assertIn("meditations/scripts/select_design.py", sources)
        self.assertEqual(len([name for name in sources if name.endswith(".css")]), 5)

    def test_archive_is_reproducible_and_matches_every_member(self):
        sources = package.read_sources()
        payload = package.build_archive(sources)
        self.assertEqual(package.build_archive(sources), payload)
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            self.assertEqual(set(archive.namelist()), set(sources))
            self.assertIsNone(archive.testzip())
            for name, contents in sources.items():
                self.assertEqual(archive.read(name), contents)

    def test_root_download_is_current(self):
        self.assertEqual(package.ARCHIVE.read_bytes(), package.build_archive(package.read_sources()))

    def test_description_accepts_upload_boundary(self):
        package.validate_description("name: meditations\ndescription: " + "a" * 200)

    def test_description_rejects_missing_empty_duplicate_and_overlong_values(self):
        for value in ["name: meditations", "description: ", "description: " + "a" * 201,
                      "description: first\ndescription: second"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                package.validate_description(value)

    def test_description_rejects_yaml_forms_that_need_decoding(self):
        for value in ["description: >-\n  folded text", "description: |\n  literal text",
                      'description: "quoted"', "description: [list]",
                      "description: text # comment", "description: first\n  continuation"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                package.validate_description(value)


if __name__ == "__main__":
    unittest.main()
