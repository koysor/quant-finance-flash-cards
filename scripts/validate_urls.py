"""Validate all URLs in resources.json.

Sends async HEAD requests (falling back to GET on 405) to every URL.
For YouTube URLs, performs a deeper check to detect "Video Unavailable" pages
which normally return 200 OK.

Exits non-zero if any URL is unreachable, which blocks the commit.
"""

import asyncio
import json
import subprocess
import sys
import re
from pathlib import Path

import aiohttp

RESOURCES_PATH = Path(__file__).resolve().parent.parent / "resources.json"
CONCURRENCY = 20
TIMEOUT = aiohttp.ClientTimeout(total=20)
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


async def check_youtube_availability(session, url):
    """Deep check for YouTube video availability."""
    try:
        async with session.get(url, timeout=TIMEOUT) as resp:
            if resp.status != 200:
                return False
            html = await resp.text()
            
            # YouTube specific indicators of unavailability
            unavailable_markers = [
                '"status":"ERROR"',
                '"reason":"Video unavailable"',
                '"reason":"This video is private"',
                '"reason":"This video has been removed by the uploader"',
                '<div id="player-error-message"',
                'class="yt-player-error-message-renderer"',
                'video is unavailable',
                'video is private'
            ]
            
            for marker in unavailable_markers:
                if marker in html or marker.lower() in html.lower():
                    return False
            
            # If we find "status":"OK" in the player response, it's definitely fine
            if '"status":"OK"' in html:
                return True
                
            return True # Assume OK if no error markers found
    except:
        return False


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

    # Domains that block automated requests regardless of method — treat as always OK.
    SKIP_DOMAINS = ("www.investopedia.com", "financeunlocked.com")
    if any(domain in url for domain in SKIP_DOMAINS):
        return card_id, category, title, url, True

    async with semaphore:
        # Special handling for YouTube
        if "youtube.com/watch?v=" in url:
            ok = await check_youtube_availability(session, url)
            return card_id, category, title, url, ok

        try:
            # General URL check
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
    try:
        with open(RESOURCES_PATH) as f:
            resources = json.load(f)
    except Exception as e:
        print(f"Error reading resources.json: {e}")
        return 1

    tasks = []
    semaphore = asyncio.Semaphore(CONCURRENCY)
    headers = {"User-Agent": USER_AGENT}

    async with aiohttp.ClientSession(headers=headers) as session:
        for card_id, sections in resources.items():
            if not isinstance(sections, dict):
                continue
            for category, entries in sections.items():
                if not isinstance(entries, list):
                    continue
                for entry in entries:
                    if not isinstance(entry, dict) or "url" not in entry:
                        continue
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
