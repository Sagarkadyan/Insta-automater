#!/data/data/com.termux/files/usr/bin/bash
set -e


cd /storage/emulated/0/automater/scripts
echo "running link fetcher"

nohup python link_fitcher.py > /dev/null 2>1 &

FEATCHER_PID=$!
sleep 10
kill -9 $FEATCHER_PID
echo "sleepinh for 60 sec"
 
echo "killing process"


# 1. Collect Instagram metadata
echo "[1/4] Running metadata_collector.py..."
python metadata_collector.py

# 2. Download videos
echo "[2/4] Running video_downloader_android.py..."
python video_downloader_android.py

# 3. [Add your converter script if needed]
# echo "[3/4] Running converter.py..."
# python converter.py

# 4. Prepare manual upload (prints/share/copy to clipboard)
echo "[4/4] Running manual_instagram_uploader.py..."
python uploader.py

echo "[✓] All scripts finished successfully!"


