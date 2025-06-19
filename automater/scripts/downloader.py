import os
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SORTED_LINKS_DIR = BASE_DIR / "data" / "sorted  reels" # Changed to match metadata_collector.py
ARCHIVE_DIR = BASE_DIR / "Data"
VIDEO_DIR = Path("~/Documents/automater/Downloads/videos").expanduser()
PROCESSED_FILE = Path("~/Documents/automater/Downloads/processed_links.txt").expanduser()

VIDEO_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_FILE.touch(exist_ok=True)


def read_processed():
    with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())


def mark_processed(link):
    with open(PROCESSED_FILE, "a", encoding="utf-8") as f:
        f.write(link + "\n")


def extract_shortcode(url):
    import re
    match = re.search(r"/reel/([\w-]+)/", url)
    return match.group(1) if match else None


def download_video(url, shortcode):
    # You can replace this with yt-dlp or any tool you prefer
    output_path = VIDEO_DIR / f"{shortcode}.mp4"
    print(f"[INFO] Downloading {url} as {output_path.name}...")

    # Using yt-dlp
    result = os.system(
        f"yt-dlp -f best -o \"{output_path}\" {url} > /dev/null 2>&1"
    )

    if output_path.exists():
        print(f"[OK] Saved to {output_path}")
        return True
    else:
        print(f"[ERROR] Failed to download: {url}")
        return False


def main():
    processed = read_processed()

    for file in SORTED_LINKS_DIR.glob("*.txt"):
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
