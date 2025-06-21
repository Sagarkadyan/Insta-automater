#!/bin/bash

# Base directory
BASE_DIR="$HOME/Documents/automater"
SCRIPTS_DIR="$BASE_DIR/scripts"
LOG_DIR="$BASE_DIR/logs"
VENV_DIR="/home/sagar/Documents/hacking-/venv"  # Assuming you have a venv directory in your base directory
DEPENDENCY_FILE="$BASE_DIR/dependencies.txt" # Assuming you have a dependencies.txt file

# Create log directory if not exists
mkdir -p "$LOG_DIR"

# Function to log messages
log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
  log "[ERROR] Virtual environment not found at $VENV_DIR. Please create it."
  exit 1
fi

# Activate virtual environment
log "[INFO] Activating virtual environment..."
source "$VENV_DIR/bin/activate"



# Check if all required Python scripts exist
for script in "$SCRIPTS_DIR/link_fitcher.py" "$SCRIPTS_DIR/metadata_collector.py" "$SCRIPTS_DIR/downloader.py" "$SCRIPTS_DIR/uploader.py"; do
  if [ ! -f "$script" ]; then
    log "[ERROR] Required script not found: $script"
    exit 1
  fi
done

log "[INFO] Starting full automation pipeline..."

# 1. Link Fetcher
log "[STEP 1] Running LinkFetcher..."
python3 "$SCRIPTS_DIR/link_fitcher.py" >> "$LOG_DIR/fetch.log" 2>&1

# 2. Metadata Collector
log "[STEP 2] Running MetadataCollector..."
python3 "$SCRIPTS_DIR/metadata_collector.py" >> "$LOG_DIR/fetch.log" 2>&1

# 3. Downloader
log "[STEP 3] Running Downloader..."
python3 "$SCRIPTS_DIR/downloader.py" >> "$LOG_DIR/download.log" 2>&1

# 4. Uploader
UPLOAD_COUNT=${1:-1}
log "[STEP 5] Running Uploader (count=$UPLOAD_COUNT)..."
python3 "$SCRIPTS_DIR/uploader.py" "$UPLOAD_COUNT" >> "$LOG_DIR/upload.log" 2>&1

log "[INFO] Automation run complete."

# Deactivate virtual environment (optional)
deactivate
