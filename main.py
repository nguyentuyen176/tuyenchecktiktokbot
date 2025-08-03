import time
import schedule
from datetime import datetime
from telegram import Bot

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=BOT_TOKEN)

def check_tiktok():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"✅ TikTok Bot Báo Cáo: {now}\n👉 Kênh @oi94qx vẫn hoạt động bình thường."
    bot.send_message(chat_id=CHAT_ID, text=message)

schedule.every().day.at("20:00").do(check_tiktok)

while True:
    schedule.run_pending()
    time.sleep(30)
