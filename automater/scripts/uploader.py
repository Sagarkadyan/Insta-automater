import os
import shutil

# Define Android storage paths
CONVERTED_DIR = "/storage/emulated/0/automater/Converted"
CAPTIONS_DIR = "/storage/emulated/0/automater/Captions"
UPLOAD_LOG = "/storage/emulated/0/automater/upload.log"
SHARE_READY_DIR = "/storage/emulated/0/automater/ToUpload"

os.makedirs(SHARE_READY_DIR, exist_ok=True)

def already_uploaded(shortcode):
    if not os.path.exists(UPLOAD_LOG):
        return False
    with open(UPLOAD_LOG) as f:
        return shortcode in f.read()

def mark_uploaded(shortcode):
    with open(UPLOAD_LOG, "a") as f:
        f.write(shortcode + "\n")

def prepare_for_share(shortcode):
    video_path = os.path.join(CONVERTED_DIR, f"temp_{shortcode}.mp4")
    caption_path = os.path.join(CAPTIONS_DIR, f"{shortcode}.txt")

    if not os.path.exists(video_path):
        print(f"[❌] Converted video not found: {video_path}")
        return

    shutil.copy(video_path, os.path.join(SHARE_READY_DIR, f"{shortcode}.mp4"))
    if os.path.exists(caption_path):
        shutil.copy(caption_path, os.path.join(SHARE_READY_DIR, f"{shortcode}.txt"))

    print(f"[✅] Ready to upload via SHARE menu:\n  Video: {shortcode}.mp4\n  Caption: {shortcode}.txt")
    mark_uploaded(shortcode)

if __name__ == "__main__":
    shortcodes = [f[5:-4] for f in os.listdir(CONVERTED_DIR) if f.startswith("temp_") and f.endswith(".mp4")]
    for code in shortcodes:
        if not already_uploaded(code):
            prepare_for_share(code)
