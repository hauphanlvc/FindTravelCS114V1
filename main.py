from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
import logging
################
from config import TOKEN, PORT


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hey, Bot Hậu đây :)) ")
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ý bạn là gì vậy , mình hông hiểu , bạn đi ra đi :))")

def main():
  # PORT = int(os.environ.get('PORT', '8443'))
  updater = Updater(TOKEN, use_context=True)
  dispatcher = updater.dispatcher
  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
  start_handler = CommandHandler('start', start)
  dispatcher.add_handler(start_handler)

# không biết người ta làm gì

  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(unknown_handler)

  # updater.start_polling()
  updater.start_webhook("0.0.0.0",PORT,TOKEN,webhook_url='https://doancs114.herokuapp.com/'+TOKEN)
  updater.idle()
# nguồn kham khảo : https://smartengines.com/building-an-ocr-bot-in-5-minutes-using-python/
if __name__ == '__main__':
    main()
