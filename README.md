
# Insta-automater — Automater Module

![Python](https://img.shields.io/badge/language-Python-blue.svg)
![Repo Size](https://img.shields.io/github/repo-size/Sagarkadyan/Insta-automater)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.7%2B-green.svg)](https://www.python.org/)  

---

## 🚀 About This Module

This folder contains the core automation scripts for **Insta-automater**. Use these scripts to automate Instagram activitie of uploading reel, by sharing to bot while you scroll the reel.

---


## 📂 Folder Structure

| Folder/File       | Purpose                                                        |
|-------------------|----------------------------------------------------------------|
| `Archive/`        | Old or backup files and scripts                                |
| `Downloads/`      | Holds downloaded Instagram media and related files             |
| `SortedLinks/`    | Stores collections of processed or sorted Instagram links      |
| `ToUpload/`       | Queued files ready for uploading to Instagram                  |
| `data/`           | Contains data files required or produced by automation scripts |
| `logs/`           | Stores logs from automation runs and script outputs            |
| `scripts/`        | Main automation scripts (Python and Shell)                     |
| `sessions/`       | Session files for authentication and persistent logins         |

---

## ⚙️ Key Automation Scripts (`scripts/`)

- **downloader.py** — Downloads media from Instagram.
- **uploader.py** — Uploads media to Instagram.
- **metadata_collector.py** — Extracts metadata from Instagram content.
- **link_fitcher.py** — Processes and manages Instagram links.
- **converter.py** — Converts media/data to required formats.
- **sesiongen.py** — Generates session files for automation.
- **runner.sh** / **andriod_runner.sh** — Shell scripts to automate and schedule tasks.

## 📦 Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Sagarkadyan/Insta-automater.git
    cd Insta-automater/automater
    ```

2. **Install Dependencies**

    Make sure you have Python 3.7+ installed.  
    Then install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

---

## ⚙️ Automation Scripts — Purpose & Usage

Navigate to the `automater/scripts/` folder before running these commands.

### Python Scripts

- **downloader.py**  
  _Purpose:_ Download Instagram media (photos/videos) using predefined links or credentials.  
  _Usage:_  
  ```bash
  python downloader.py
  ```
  This will start the media download process. Make sure links or targets are configured inside the script or via input files.

- **uploader.py**  
  _Purpose:_ Upload photos or videos to Instagram from the `ToUpload/` folder or a specified source.  
  _Usage:_  
  ```bash
  python uploader.py
  ```
  Configure your credentials and specify upload parameters as needed in the script.

- **metadata_collector.py**  
  _Purpose:_ Fetch and save metadata (like captions, hashtags, user info, etc.) for Instagram content.  
  _Usage:_  
  ```bash
  python metadata_collector.py
  ```
  Outputs metadata to a file or prints to console, depending on script settings.

- **link_fitcher.py**  
  _Purpose:_ Extract and process Instagram post links from Telegram that you share to your bot while scrolling  .  
  _Usage:_  
  ```bash
  python link_fitcher.py
  ```
  Processes input sources and writes sorted/filtered links to the `SortedLinks/` folder.

- **converter.py**  
  _Purpose:_ Convert media files (e.g., format, resolution) as needed for downloading/uploading.  
  _Usage:_  
  ```bash
  python converter.py
  ```
  Configure source and output settings inside the script.

- **sesiongen.py**  
  _Purpose:_ Generate and save Instagram login session files for automated scripts.  
  _Usage:_  
  ```bash
  python sesiongen.py
  ```
  Follow prompts or configure credentials in the script.

### Shell Scripts

- **runner.sh**  
  _Purpose:_ Orchestrate and automate a sequence of Python scripts for a full workflow (download, process, upload, etc.) in Linux.  
  _Usage:_  
  ```bash
  bash runner.sh
  ```
  You may need to make this file executable first with `chmod +x runner.sh`.

- **andriod_runner.sh**  
  _Purpose:_ Specialized runner for Android automation environments or emulators on android using Termux.  
  _Usage:_  
  ```bash
  bash andriod_runner.sh
  ```
  Again, run `chmod +x andriod_runner.sh` if needed.

---

## 📝 Notes

- Each script may require some configuration (such as credentials or file paths) inside the code.
- Output and logs are generally saved in their respective folders.
- Make sure you have all dependencies (see `requirements.txt` if present).

---

## ⚠️ Disclaimer

- Use responsibly and at your own risk.
- Automating Instagram may violate their terms of service.

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue to discuss any major changes.

---

## 📄 License

This project is licensed under the MIT License.

---

## 💬 Support

If you have questions, open an issue on this repository.
