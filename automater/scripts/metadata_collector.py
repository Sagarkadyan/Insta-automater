import instaloader
from pathlib import Path

# --- CONFIGURATION ---
USERNAME = "your_instagram_username"  # <--- Set your Instagram username here

SESSION_FILE = f"/storage/emulated/0/automater/sessions/{USERNAME}.session"
LINKS_FILE = Path("/storage/emulated/0/automater/data/fetched_links.txt")

def extract_shortcode(url):
    if "reel/" in url:
        return url.split("reel/")[1].split("/")[0]
    return None

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
                print(f"Audio: {post.audio_url if post.has_audio else 'No audio'}")
                print(f"URL: {url}")
            except Exception as e:
                print(f"[✘] Failed to fetch {shortcode}: {e}")

if __name__ == "__main__":
    if not LINKS_FILE.exists():
        print(f"File not found: {LINKS_FILE}")
        exit(1)
    collect_metadata_from_urls(str(LINKS_FILE), USERNAME)
