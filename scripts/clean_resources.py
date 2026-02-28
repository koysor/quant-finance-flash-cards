import json

# List of broken URLs from the check_youtube.py output
BROKEN_URLS = {
    "https://www.youtube.com/watch?v=syMwhIAacOE",
    "https://www.youtube.com/watch?v=TnS8kI7jSXw",
    "https://www.youtube.com/watch?v=3bEOTaXSXsg",
    "https://www.youtube.com/watch?v=HCgunMYe5kI",
    "https://www.youtube.com/watch?v=tEYCsVrI6TQ",
    "https://www.youtube.com/watch?v=UFWGeK7dKxk",
    "https://www.youtube.com/watch?v=R8DnwPNssXk",
    "https://www.youtube.com/watch?v=kz4wm3EvYnI",
    "https://www.youtube.com/watch?v=B7KAi8y8Cr0",
    "https://www.youtube.com/watch?v=NXo3NBjIt8E",
    "https://www.youtube.com/watch?v=Am8ydVVpjQk",
    "https://www.youtube.com/watch?v=aM-URjMeFuY",
    "https://www.youtube.com/watch?v=KGnMSsdHJmA",
    "https://www.youtube.com/watch?v=nUDEBxMWrdM",
    "https://www.youtube.com/watch?v=b4nDApRwzwI",
    "https://www.youtube.com/watch?v=omgUjsGXrKY",
    "https://www.youtube.com/watch?v=2ig7mA1KSLU",
    "https://www.youtube.com/watch?v=0GJnA-ABXQ8",
    "https://www.youtube.com/watch?v=cKzTlHRPfkQ",
    "https://www.youtube.com/watch?v=1ZfDHkBhMKM",
    "https://www.youtube.com/watch?v=AM-mkdbSxnA",
    "https://www.youtube.com/watch?v=6cS_O1GSmHk",
    "https://www.youtube.com/watch?v=shGYBVsQJwQ",
    "https://www.youtube.com/watch?v=LQRTdYJkjnM",
    "https://www.youtube.com/watch?v=JF1_UiKFJMs",
    "https://www.youtube.com/watch?v=YAlJCEDp768",
    "https://www.youtube.com/watch?v=AOFi5dEpJx0",
    "https://www.youtube.com/watch?v=z3XaFfMFRBg",
    "https://www.youtube.com/watch?v=ISaVvSxFMHk",
    "https://www.youtube.com/watch?v=2p2AcoRdBuE",
    "https://www.youtube.com/watch?v=lMGMEfKvL7E"
}

def main():
    try:
        with open('resources.json', 'r') as f:
            resources = json.load(f)
    except FileNotFoundError:
        print("resources.json not found")
        return

    removed_count = 0
    
    for card_id, data in resources.items():
        if 'videos' in data:
            original_len = len(data['videos'])
            data['videos'] = [v for v in data['videos'] if v['url'] not in BROKEN_URLS]
            removed_count += (original_len - len(data['videos']))

    print(f"Removed {removed_count} broken video links.")

    with open('resources.json', 'w') as f:
        json.dump(resources, f, indent=2, ensure_ascii=False)
        f.write('\n')

if __name__ == "__main__":
    main()
