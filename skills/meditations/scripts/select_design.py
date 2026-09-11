#!/usr/bin/env python3
"""Select a bundled study design offline and print one JSON object.

Paths in the result are relative to the meditations skill directory. The
selector reads only its bundled registry and CSS and never saves history.
"""

import argparse
import json
from pathlib import Path
import random
import re
import sys


SKILL_ROOT = Path(__file__).resolve().parents[1]
REGISTRY = SKILL_ROOT / "assets" / "design-systems" / "registry.json"
KINDS = ("comparison", "process", "concept", "decision")
MAX_EXCLUSIONS = 3


def load_registry(path=REGISTRY):
    """Validate the bundled catalogue before allowing a selection."""
    path = Path(path)
    if path.is_symlink():
        raise ValueError("The design registry must be a regular bundled file")
    catalogue = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(catalogue, dict) or catalogue.get("version") != 1:
        raise ValueError("Unsupported design registry version")
    systems = catalogue.get("systems")
    if not isinstance(systems, list) or not systems:
        raise ValueError("The design registry must contain systems")
    seen = set()
    for system in systems:
        if not isinstance(system, dict):
            raise ValueError("Each design entry must be an object")
        design_id = system.get("id")
        if not isinstance(design_id, str) or not re.fullmatch(r"[a-z]+(?:-[a-z]+)*", design_id):
            raise ValueError("Invalid design ID")
        if design_id in seen:
            raise ValueError("Duplicate design ID")
        seen.add(design_id)
        if any(not isinstance(system.get(key), str) or not system[key].strip()
               for key in ("name", "brief", "css")):
            raise ValueError("Each design requires a name, brief and CSS path")
        expected = f"assets/design-systems/{design_id}.css"
        if system["css"] != expected:
            raise ValueError("A CSS path does not match its bundled design ID")
        css_path = path.parent / f"{design_id}.css"
        if css_path.is_symlink() or not css_path.is_file():
            raise ValueError(f"Bundled CSS is missing or is a symlink: {design_id}")
        if not css_path.read_text(encoding="utf-8").strip():
            raise ValueError(f"Bundled CSS is empty: {design_id}")
        kinds = system.get("kinds")
        if (not isinstance(kinds, list) or not kinds
                or any(item not in KINDS for item in kinds)
                or len(kinds) != len(set(kinds))):
            raise ValueError(f"Invalid study kinds: {design_id}")
    return systems


def select_design(systems, *, seed=None, exclude=(), kind=None):
    """Choose uniformly among eligible systems, using system randomness by default.

    Call with the validated result of load_registry(). Stale IDs in recent
    history are reported and ignored. If exclusions exhaust the eligible pool,
    reset only the exclusions, retaining the requested study kind.
    """
    exclude = tuple(exclude)
    if len(exclude) > MAX_EXCLUSIONS:
        raise ValueError("Pass at most three recent design IDs")
    if kind is not None and kind not in KINDS:
        raise ValueError("Unknown study kind")
    if not systems:
        raise ValueError("No design systems are available")
    known_ids = {system["id"] for system in systems}
    excluded_ids = list(dict.fromkeys(item for item in exclude if item in known_ids))
    ignored = list(dict.fromkeys(item for item in exclude if item not in known_ids))
    eligible = [system for system in systems if kind is None or kind in system["kinds"]]
    if not eligible:
        raise ValueError("No design systems support the requested study kind")
    remaining = [system for system in eligible if system["id"] not in excluded_ids]
    reset = not remaining
    if reset:
        remaining = eligible
    rng = random.SystemRandom() if seed is None else random.Random(seed)
    chosen = rng.choice(remaining)
    return {
        "id": chosen["id"],
        "name": chosen["name"],
        "css": chosen["css"],
        "brief": chosen["brief"],
        "selection_method": "system-random" if seed is None else "seeded",
        "kind": kind,
        "excluded_ids": excluded_ids,
        "ignored_exclusions": ignored,
        "exclusions_reset": reset,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, help="use a repeatable integer seed for testing")
    parser.add_argument("--exclude", action="append", default=[], metavar="ID",
                        help="exclude a recent choice; repeat at most three times")
    parser.add_argument("--kind", choices=KINDS, help="limit selection to a suitable study kind")
    args = parser.parse_args(argv)
    try:
        result = select_design(load_registry(), seed=args.seed,
                               exclude=args.exclude, kind=args.kind)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Design selection error: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
