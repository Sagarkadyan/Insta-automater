import os
import re
from pathlib import Path

# Use the *actual* Android internal storage location
BASE_DIR = Path("/storage/emulated/0/automater")
SORTED_LINKS_DIR = BASE_DIR / "data" / "sorted reels"
VIDEO_DIR = BASE_DIR / "Downloads"  # Save videos here
PROCESSED_FILE = BASE_DIR / "data" / "processed_links.txt"

# Ensure directories exist
VIDEO_DIR.mkdir(parents=True, exist_ok=True)
SORTED_LINKS_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_FILE.touch(exist_ok=True)

def read_processed():
    with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def mark_processed(link):
    with open(PROCESSED_FILE, "a", encoding="utf-8") as f:
        f.write(link + "\n")

def extract_shortcode(url):
    match = re.search(r"/reel/([\w-]+)/", url)
    return match.group(1) if match else None

def download_video(url, shortcode):
    output_path = VIDEO_DIR / f"{shortcode}.mp4"
    print(f"[INFO] Downloading {url} as {output_path.name}...")

    # Use yt-dlp for downloading
    result = os.system(
        f"yt-dlp -f best -o \"{output_path}\" {url} > /dev/null 2>&1"
    )

    if output_path.exists() and output_path.stat().st_size > 0:
        print(f"[OK] Saved to {output_path}")
        return True
    else:
        print(f"[ERROR] Failed to download: {url}")
        return False

def main():
    processed = read_processed()
    files = list(SORTED_LINKS_DIR.glob("*.txt"))
    if not files:
        print(f"[WARN] No input txt files found in {SORTED_LINKS_DIR}")
        return

    for file in files:
        if file.name == "processed_links.txt":
            continue

        with open(file, "r", encoding="utf-8") as f:
            for url in f:
                url = url.strip()
                if not url or url in processed:
                    continue

                shortcode = extract_shortcode(url)
                if not shortcode:
                    print(f"[SKIP] Invalid URL: {url}")
                    continue

                if download_video(url, shortcode):
                    mark_processed(url)

if __name__ == "__main__":
    main()
