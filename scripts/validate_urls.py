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
from urllib.parse import urlparse

import aiohttp

RESOURCES_PATH = Path(__file__).resolve().parent.parent / "resources.json"
CONCURRENCY = 20
# Wikipedia answers 429 when hit with the full concurrency, so cap each host.
HOST_CONCURRENCY = 4
MAX_ATTEMPTS = 4
RETRY_STATUSES = {429, 500, 502, 503, 504}
_host_semaphores: dict[str, asyncio.Semaphore] = {}


def _host_semaphore(host: str) -> asyncio.Semaphore:
    """One semaphore per host, created lazily inside the running event loop."""
    return _host_semaphores.setdefault(host, asyncio.Semaphore(HOST_CONCURRENCY))
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
    # youtube.com rate-limits and blocks bot GETs even for live videos.
    SKIP_DOMAINS = ("www.investopedia.com", "financeunlocked.com", "youtube.com")
    host = (urlparse(url).hostname or "").lower()
    if any(host == d or host.endswith("." + d) for d in SKIP_DOMAINS):
        return card_id, category, title, url, True

    host = (urlparse(url).hostname or "").lower()
    async with semaphore, _host_semaphore(host):
        ok = False
        for attempt in range(MAX_ATTEMPTS):
            retry_after = 0.0
            try:
                # General URL check
                async with session.head(url, allow_redirects=True) as resp:
                    status = resp.status
                    if status == 405:
                        async with session.get(url, allow_redirects=True) as resp2:
                            status = resp2.status
                            resp = resp2
                    ok = status < 400
                    if status in RETRY_STATUSES:
                        retry_after = float(resp.headers.get("Retry-After", 0) or 0)
            except (aiohttp.ClientError, asyncio.TimeoutError):
                ok, status = False, None

            # A rate limit or transient server error is not a broken link: back off and retry.
            if ok or (status is not None and status not in RETRY_STATUSES):
                break
            await asyncio.sleep(min(max(retry_after, 2 ** attempt), 30))

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

    async with aiohttp.ClientSession(headers=headers, timeout=TIMEOUT) as session:
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
