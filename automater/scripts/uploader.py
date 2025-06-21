import os
import shutil
import subprocess

# Paths
DOWNLOADS_DIR = "/storage/emulated/0/automater/Downloads"
TOUPLOAD_DIR = "/storage/emulated/0/automater/ToUpload"
UPLOAD_LOG = "/storage/emulated/0/automater/upload.log"
ANIME_CAPTION_FILE = "/storage/emulated/0/automater/animecaption.txt"
METADATA_FILE = "/storage/emulated/0/automater/data/fetched_links.txt"  # Output of metadata_collector

os.makedirs(TOUPLOAD_DIR, exist_ok=True)

def already_uploaded(shortcode):
    if not os.path.exists(UPLOAD_LOG):
        return False
    with open(UPLOAD_LOG) as f:
        return shortcode in f.read()

def mark_uploaded(shortcode):
    with open(UPLOAD_LOG, "a") as f:
        f.write(shortcode + "\n")

def get_metadata_for_shortcode(shortcode):
    # Reads the metadata file and returns the line for this shortcode, if present
    if not os.path.exists(METADATA_FILE):
        return ""
    with open(METADATA_FILE, encoding="utf-8") as f:
        for line in f:
            if shortcode in line:
                return line
    return ""

def copy_caption_to_clipboard(caption_file):
    # Use Termux clipboard utility
    with open(caption_file, "r", encoding="utf-8") as f:
        caption = f.read()
    subprocess.run(["termux-clipboard-set"], input=caption.encode(), check=True)
    print("[✅] Anime caption copied to clipboard.")

def prepare_for_upload(shortcode):
    video_path = os.path.join(DOWNLOADS_DIR, f"{shortcode}.mp4")
    if not os.path.exists(video_path):
        print(f"[❌] Video not found: {video_path}")
        return

    # Check metadata for this shortcode
    meta = get_metadata_for_shortcode(shortcode)
    if "anime" in meta.lower():
        if os.path.exists(ANIME_CAPTION_FILE):
            copy_caption_to_clipboard(ANIME_CAPTION_FILE)
        else:
            print("[⚠️] Anime caption file not found.")
    else:
        print("[ℹ️] Not anime content, no caption copied.")

    # Copy video to ToUpload directory
    shutil.copy(video_path, os.path.join(TOUPLOAD_DIR, f"{shortcode}.mp4"))
    print(f"[✅] Ready to upload via SHARE menu: {shortcode}.mp4")
    mark_uploaded(shortcode)

if __name__ == "__main__":
    # Pick up all mp4s in the Downloads folder
    all_videos = [f for f in os.listdir(DOWNLOADS_DIR) if f.endswith(".mp4")]
    for fname in all_videos:
        shortcode = fname[:-4]  # Remove .mp4
        if not already_uploaded(shortcode):
            prepare_for_upload(shortcode)
        else:
            print(f"[SKIP] Already uploaded: {shortcode}")
