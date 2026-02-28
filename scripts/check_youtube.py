import json
import asyncio
import aiohttp
import re

async def check_youtube_url(session, url, title, card_id):
    try:
        # Use a common browser user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        async with session.get(url, headers=headers, timeout=15) as response:
            if response.status != 200:
                return False, f"HTTP {response.status}"
            
            html = await response.text()
            
            # YouTube specific indicators of unavailability
            # These are often found in the "ytInitialPlayerResponse" JSON object inside the HTML
            unavailable_markers = [
                '"status":"ERROR"',
                '"reason":"Video unavailable"',
                '"reason":"This video is private"',
                '"reason":"This video has been removed by the uploader"',
                '<div id="player-error-message"',
                'class="yt-player-error-message-renderer"'
            ]
            
            for marker in unavailable_markers:
                if marker in html:
                    return False, "Confirmed Unavailable"
            
            # If we find the video title or 'playabilityStatus":{"status":"OK"', it's likely fine
            if '"status":"OK"' in html or 'playabilityStatus' in html:
                return True, "OK"

            # Fallback check for common "unavailable" text if no JSON markers found
            if "video is unavailable" in html.lower() or "video is private" in html.lower():
                return False, "Likely Unavailable"

            return True, "Potentially OK (no error markers)"
            
    except Exception as e:
        return False, f"Error: {str(e)}"

async def main():
    try:
        with open('resources.json', 'r') as f:
            resources = json.load(f)
    except FileNotFoundError:
        print("resources.json not found")
        return

    items_to_check = []
    for card_id, data in resources.items():
        for video in data.get('videos', []):
            if 'youtube.com' in video['url']:
                items_to_check.append((card_id, video))

    print(f"Checking {len(items_to_check)} YouTube URLs...")
    
    # Increase batch size and use a single session
    async with aiohttp.ClientSession() as session:
        batch_size = 5
        results = []
        for i in range(0, len(items_to_check), batch_size):
            batch = items_to_check[i:i+batch_size]
            print(f"Batch {i//batch_size + 1}/{(len(items_to_check)-1)//batch_size + 1}...")
            batch_tasks = [check_youtube_url(session, item[1]['url'], item[1]['title'], item[0]) for item in batch]
            batch_results = await asyncio.gather(*batch_tasks)
            results.extend(batch_results)
            await asyncio.sleep(0.5)

    broken = []
    for (card_id, video), (is_ok, reason) in zip(items_to_check, results):
        if not is_ok:
            broken.append((card_id, video['title'], video['url'], reason))
            print(f"BROKEN: [{card_id}] {video['title']} -> {video['url']} ({reason})")

    print(f"\nSummary: {len(broken)} broken links found.")
    
    if broken:
        print("\nTo remove these from resources.json, run a script or manually edit.")

if __name__ == "__main__":
    asyncio.run(main())
