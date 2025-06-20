from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os
from pathlib import Path

# ⚠️ Replace this with your real bot token (keep this file private!)
BOT_TOKEN = "7366166182:AAEr19QwUwtgw89NkXNSELBQg-AopvRjog0"

# Path to save links
LINKS_DIR = Path("/storage/emulated/0/automater/data")
LINKS_DIR.mkdir(parents=True, exist_ok=True)
LINK_FILE = LINKS_DIR / "fetched_links.txt"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📥 Send me any Instagram Reel link to save it locally.")

# Message handler to save links
async def save_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if "instagram.com/reel/" in text or "instagram.com/" in text:
        with open(LINK_FILE, "a", encoding="utf-8") as f:
            f.write(text + "\n")
        await update.message.reply_text("✅ Link saved to your system.")
    else:
        await update.message.reply_text("❌ Not a valid Instagram link.")

# /clearlinks command (optional)
async def clear_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    open(LINK_FILE, "w").close()
    await update.message.reply_text("🧹 All saved links have been cleared.")

# Main
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clearlinks", clear_links))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_link))

    print(f"🤖 Bot running. Saving links to: {LINK_FILE}")
    app.run_polling()
