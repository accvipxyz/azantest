import time
import random
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# ضع هنا رمز الوصول الخاص ببوتك
TOKEN = '6870143125:AAGvj2FULB8Vwn1gjeCBa4Aea7uY2j0sLiI'

# أذكار للإرسال
azkar_list = [
    "اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت وإليك المصير.",
    "الحمد لله الذي أحيانا بعد ما أماتنا وإليه النشور.",
    "اللهم ما أصبح بي من نعمة أو بأحد من خلقك فمنك وحدك لا شريك لك فلك الحمد ولك الشكر.",
    # أذكار إضافية يمكنك إضافتها هنا
]

def send_azkar(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    while True:
        azkar = random.choice(azkar_list)
        context.bot.send_message(chat_id=chat_id, text=azkar)
        time.sleep(1)

def main() -> None:
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # تعريف أمر البداية
    start_handler = CommandHandler('start', send_azkar)
    dispatcher.add_handler(start_handler)

    # بدء تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
