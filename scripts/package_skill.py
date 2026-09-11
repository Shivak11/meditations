#!/usr/bin/env python3
"""Build or check the ready-to-upload Claude skill ZIP using only the stdlib."""

import argparse
import io
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "meditations.zip"
SOURCES = {
    "meditations/SKILL.md": "skills/meditations/SKILL.md",
    "meditations/references/aliveness-review.md":
        "skills/meditations/references/aliveness-review.md",
    "meditations/references/declared-preferences.md":
        "skills/meditations/references/declared-preferences.md",
    "meditations/references/meditations-format.md":
        "skills/meditations/references/meditations-format.md",
    "meditations/references/reflection-format.md": "skills/meditations/references/reflection-format.md",
    "meditations/references/visual-study-output.md": "skills/meditations/references/visual-study-output.md",
    "meditations/references/fallback-designs.md": "skills/meditations/references/fallback-designs.md",
    "meditations/scripts/select_design.py": "skills/meditations/scripts/select_design.py",
    "meditations/assets/design-systems/registry.json": "skills/meditations/assets/design-systems/registry.json",
    "meditations/assets/design-systems/paper-notes.css": "skills/meditations/assets/design-systems/paper-notes.css",
    "meditations/assets/design-systems/colour-blocks.css": "skills/meditations/assets/design-systems/colour-blocks.css",
    "meditations/assets/design-systems/technical-diagrams.css": "skills/meditations/assets/design-systems/technical-diagrams.css",
    "meditations/assets/design-systems/editorial-study.css": "skills/meditations/assets/design-systems/editorial-study.css",
    "meditations/assets/design-systems/dark-study.css": "skills/meditations/assets/design-systems/dark-study.css",
    "meditations/LICENSE": "LICENSE",
}


def read_sources():
    """Use an explicit allowlist so unrelated repository files cannot leak in."""
    files = {}
    for destination, source in SOURCES.items():
        path = ROOT / source
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Required source is missing or is a symlink: {source}")
        files[destination] = path.read_bytes()

    skill = files["meditations/SKILL.md"].decode("utf-8")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", skill, re.S)
    if not frontmatter or not re.search(
        r"^name:\s*meditations\s*$", frontmatter.group(1), re.M
    ):
        raise ValueError("SKILL.md must declare name: meditations in its frontmatter")

    validate_description(frontmatter.group(1))

    for name, data in files.items():
        if not name.endswith(".md"):
            continue
        text = data.decode("utf-8")
        links = re.findall(r"\]\(([^)\s]+)\)", text)
        links += re.findall(r"`(references/[^`\s]+\.md)`", text)
        for link in links:
            if link.startswith("#") or re.match(r"[a-zA-Z][\w+.-]*:", link):
                continue
            target = link.split("#", 1)[0]
            resolved = posixpath.normpath(str(PurePosixPath(name).parent / target))
            if resolved not in files:
                raise ValueError(f"Unbundled relative resource in {name}: {link}")
    return files


def validate_description(frontmatter):
    """Keep this package's metadata within Claude Chat's upload limit.

    Accept a plain single-line scalar deliberately; reject YAML forms that
    would need a parser rather than guessing their decoded length.
    """
    matches = re.findall(r"^description:([^\r\n]*)$", frontmatter, re.M)
    if len(matches) != 1:
        raise ValueError("SKILL.md must declare exactly one description")
    description = matches[0].strip()
    if not description or len(description) > 200:
        raise ValueError("SKILL.md description must contain 1 to 200 characters")
    if description[0] in "|>\"'[{&*!%@`" or " #" in description or ": " in description:
        raise ValueError("Use a plain single-line description without YAML syntax")
    if re.search(r"^description:[^\r\n]*\r?\n[ \t]+\S", frontmatter, re.M):
        raise ValueError("Use a plain single-line description without continuation lines")


def build_archive(files):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name in sorted(files):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            entry.compress_type = zipfile.ZIP_STORED
            archive.writestr(entry, files[name])
    payload = buffer.getvalue()
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        if archive.namelist() != sorted(files):
            raise ValueError("Archive layout does not match the allowlist")
        if archive.testzip() is not None:
            raise ValueError("Archive failed its integrity check")
        for name, data in files.items():
            if archive.read(name) != data:
                raise ValueError(f"Archive content does not match source: {name}")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true",
        help="fail if the root meditations.zip differs from the current sources",
    )
    args = parser.parse_args()
    try:
        files = read_sources()
        payload = build_archive(files)
        if args.check:
            if not ARCHIVE.is_file() or ARCHIVE.read_bytes() != payload:
                raise ValueError(
                    "meditations.zip is missing or stale; run python3 scripts/package_skill.py"
                )
            print(f"meditations.zip matches all {len(files)} source files")
        else:
            ARCHIVE.write_bytes(payload)
            print(f"Built meditations.zip ({len(files)} files, {len(payload):,} bytes)")
    except (OSError, UnicodeError, ValueError, zipfile.BadZipFile) as error:
        print(f"Package error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
