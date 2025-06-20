#!/data/data/com.termux/files/usr/bin/bash
set -e

# Optional: activate Python virtual environment
if [ -d "/storage/emulated/0/automater/venv" ]; then
    source /storage/emulated/0/automater/venv/bin/activate
    echo "[✓] Activated Python venv."
fi

cd /storage/emulated/0/automater/scripts

# 1. Collect Instagram metadata
echo "[1/4] Running metadata_collector.py..."
python3 metadata_collector.py

# 2. Download videos
echo "[2/4] Running video_downloader_android.py..."
python3 video_downloader_android.py

# 3. [Add your converter script if needed]
# echo "[3/4] Running converter.py..."
# python converter.py

# 4. Prepare manual upload (prints/share/copy to clipboard)
echo "[4/4] Running manual_instagram_uploader.py..."
python3 manual_instagram_uploader.py

echo "[✓] All scripts finished successfully!"

# Deactivate venv (if used)
if [ -n "$VIRTUAL_ENV" ]; then
    deactivate
fi
