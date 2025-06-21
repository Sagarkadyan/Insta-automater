import instaloader
from pathlib import Path
import os

# --- CONFIGURATION ---
USERNAME = "put ypur own insta id"  # <--- Set your Instagram username here

SESSION_FILE = f"/storage/emulated/0/automater/sessions/{USERNAME}.session"
LINKS_FILE = Path("/storage/emulated/0/automater/data/fetched_links.txt")

def extract_shortcode(url):
    if "reel/" in url:
        return url.split("reel/")[1].split("/")[0]
    return None

CATEGORIES = { 
    "anime": ["anime", "naruto", "one piece", "luffy"],
    "cars": ["car", "supra", "mustang", "bmw", "drift"],
    "fitness": ["gym", "fitness", "workout", "pushup"],
    "motivation": ["motivation", "inspiration", "grind"],
    "edits": ["edit", "velocity", "slowmo"]
}
SORTED_DIR = "/storage/emulated/0/automater/SortedLinks"

def categorize_and_save(shortcode, caption):
    if not caption: 
        return 
    caption_lower = caption.lower() 
    for category, keywords in CATEGORIES.items():
        if any(word in caption_lower for word in keywords):
            out_path = os.path.join(SORTED_DIR, f"{category}.txt")
            os.makedirs(SORTED_DIR, exist_ok=True)
            with open(out_path, "a", encoding="utf-8") as f:
                f.write(f"https://www.instagram.com/reel/{shortcode}/\n")
            print(f"[📂] Sorted into: {category}")
            return
    # If no category matches
    out_path = os.path.join(SORTED_DIR, "uncategorized.txt")
    os.makedirs(SORTED_DIR, exist_ok=True)
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(f"https://www.instagram.com/reel/{shortcode}/\n")
    print(f"[📂] Sorted into: uncategorized")

def collect_metadata_from_urls(file_path, username):
    L = instaloader.Instaloader()
    session_file = f"/storage/emulated/0/automater/sessions/{username}.session"

    # Try to load session; fallback to login
    try:
        L.load_session_from_file(username, session_file)
        print("[i] Session loaded.")
    except Exception:
        print("[!] Session not found or invalid. Logging in...")
        from getpass import getpass
        password = getpass("Enter your Instagram password: ")
        L.login(username, password)
        Path(session_file).parent.mkdir(parents=True, exist_ok=True)
        L.save_session_to_file(session_file)
        print("[i] Logged in and session saved.")

    with open(file_path, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        shortcode = extract_shortcode(url)
        if shortcode:
            try:
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                print(f"[✔] Fetched: {shortcode}")
                print(f"Shortcode: {shortcode}")
                try:
                    print(f"Audio: {post.audio_url}")
                except AttributeError:
                    print("Audio: not available") 
                print(f"URL: {url}")
                # Add caption categorization & saving
                categorize_and_save(shortcode, post.caption)
            except Exception as e:
                print(f"[✘] Failed to fetch {shortcode}: {e}")

if __name__ == "__main__":
    if not LINKS_FILE.exists():
        print(f"File not found: {LINKS_FILE}")
        exit(1)
    collect_metadata_from_urls(str(LINKS_FILE), USERNAME)
