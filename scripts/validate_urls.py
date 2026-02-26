"""Validate all URLs in resources.json.

Sends async HEAD requests (falling back to GET on 405) to every URL.
Exits non-zero if any URL is unreachable, which blocks the commit.

When called from a git hook context, skips validation unless
resources.json is in the staged files.
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path

import aiohttp

RESOURCES_PATH = Path(__file__).resolve().parent.parent / "resources.json"
CONCURRENCY = 20
TIMEOUT = aiohttp.ClientTimeout(total=15)
USER_AGENT = (
    "Mozilla/5.0 (compatible; URLValidator/1.0; "
    "+https://github.com/koysor/quant-finance-flash-cards)"
)


def resources_staged() -> bool:
    """Return True if resources.json is in the git staging area."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True,
            text=True,
            check=True,
        )
        return "resources.json" in result.stdout.splitlines()
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Not in a git repo or git not available — run anyway
        return True


async def check_url(
    session: aiohttp.ClientSession,
    semaphore: asyncio.Semaphore,
    card_id: str,
    category: str,
    entry: dict,
) -> tuple[str, str, str, str, bool]:
    """Check a single URL. Returns (card_id, category, title, url, ok)."""
    url = entry["url"]
    title = entry["title"]
    async with semaphore:
        try:
            async with session.head(url, allow_redirects=True) as resp:
                if resp.status == 405:
                    async with session.get(url, allow_redirects=True) as resp2:
                        ok = resp2.status < 400
                else:
                    ok = resp.status < 400
        except (aiohttp.ClientError, asyncio.TimeoutError):
            ok = False
    return card_id, category, title, url, ok


async def main() -> int:
    with open(RESOURCES_PATH) as f:
        resources = json.load(f)

    tasks = []
    semaphore = asyncio.Semaphore(CONCURRENCY)
    headers = {"User-Agent": USER_AGENT}

    async with aiohttp.ClientSession(timeout=TIMEOUT, headers=headers) as session:
        for card_id, sections in resources.items():
            for category, entries in sections.items():
                for entry in entries:
                    tasks.append(
                        check_url(session, semaphore, card_id, category, entry)
                    )

        results = await asyncio.gather(*tasks)

    failures = [r for r in results if not r[4]]
    passed = len(results) - len(failures)

    if failures:
        print(f"\n\033[31m{len(failures)} broken URL(s) found:\033[0m\n")
        for card_id, category, title, url, _ in failures:
            print(f"  [{card_id}] ({category}) {title}")
            print(f"    {url}\n")
        print(f"{passed}/{len(results)} URLs OK, {len(failures)} FAILED")
        return 1

    print(f"\033[32m{passed}/{len(results)} URLs OK\033[0m")
    return 0


if __name__ == "__main__":
    # When run directly (not as a module), check git staging
    if "--force" not in sys.argv and not resources_staged():
        print("resources.json not staged — skipping URL validation")
        sys.exit(0)

    sys.exit(asyncio.run(main()))
