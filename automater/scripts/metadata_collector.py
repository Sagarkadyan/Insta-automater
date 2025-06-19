import os
import instaloader

def extract_shortcode(url):
    if "reel/" in url:
        return url.split("reel/")[1].split("/")[0]
    return None

def collect_metadata_from_urls(file_path):
    L = instaloader.Instaloader()
    L.login("your_username", "your_password")  # Replace or modify for session file if needed

    with open(file_path, "r") as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]

    for url in urls:
        shortcode = extract_shortcode(url)
        if shortcode:
            try:
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                print(f"[✔] Fetched: {shortcode}")
                print(f"Shortcode: {shortcode}")
                print(f"Audio: {post.audio_url if post.has_audio else 'No audio'}")
                print(f"URL: {url}")
            except Exception as e:
                print(f"[✘] Failed to fetch {shortcode}: {e}")

if __name__ == "__main__":
    input_file = "reels.txt"
    if os.path.exists(input_file):
        collect_metadata_from_urls(input_file)
    else:
        print("reels.txt not found.")

