#!/usr/bin/env python3
"""
Render the flash cards site to static files (see ``app/static_site.py``).

    uv run python scripts/build_static.py --prefix /flashcards --out dist

``--prefix`` is the path the site is served under (production: ``/flashcards``;
leave it empty to serve from the root).  ``--out`` is emptied first, but only if
it is empty or holds a previous build.
"""

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--prefix", default="/flashcards", help="URL prefix (default: /flashcards)"
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "dist",
        help="output directory (default: dist)",
    )
    args = parser.parse_args()

    # No secrets are used while rendering; create_app() only insists one is set.
    os.environ.setdefault("SECRET_KEY", "static-build")
    if os.environ.get("ALLOW_EDGE_EDIT") == "1":
        parser.error("unset ALLOW_EDGE_EDIT: edit mode puts edit forms in the pages")

    from app import create_app
    from app.static_site import BuildError, build

    app = create_app()
    try:
        result = build(app, args.out.resolve(), args.prefix)
    except BuildError as e:
        print(f"Static build failed: {e}", file=sys.stderr)
        return 1
    print(
        f"Rendered {result.pages} pages into {result.out}: "
        f"{result.files} files, {result.bytes / 1e6:.0f} MB, {result.seconds:.0f} s"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
