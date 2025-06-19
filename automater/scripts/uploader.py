import os

UPLOAD_LOG = "/storage/emulated/0/automater/upload.log"
CONVERTED_DIR = "/storage/emulated/0/automater/Converted"
CAPTIONS_DIR = "/storage/emulated/0/automater/Captions"

def already_uploaded(shortcode):
    if not os.path.exists(UPLOAD_LOG):
        return False
    with open(UPLOAD_LOG) as f:
        return shortcode in f.read()

def mark_uploaded(shortcode):
    with open(UPLOAD_LOG, "a") as f:
        f.write(shortcode + "\n")

def manual_upload(shortcode):
    video_path = os.path.join(CONVERTED_DIR, f"temp_{shortcode}.mp4")
    caption_path = os.path.join(CAPTIONS_DIR, f"{shortcode}.txt")

    if not os.path.exists(video_path):
        print(f"[❌] Converted video not found: {video_path}")
        return

    print(f"[🚀] READY TO UPLOAD:\nVideo: {video_path}\nCaption: {caption_path}")
    print("👉 Use Android 'Share' option to upload manually.")

    mark_uploaded(shortcode)

if __name__ == "__main__":
    shortcodes = [f[5:-4] for f in os.listdir(CONVERTED_DIR) if f.startswith("temp_") and f.endswith(".mp4")]
    for code in shortcodes:
        if not already_uploaded(code):
            manual_upload(code)
