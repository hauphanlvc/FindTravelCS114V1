from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
import logging
################
from config import TOKEN


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="ý bạn là gì vậy , mình hông hiểu , bạn đi ra đi :))")

def main():
  # PORT = int(os.environ.get('PORT', '8443'))
  updater = Updater(TOKEN, use_context=True)
  dispatcher = updater.dispatcher
  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
  start_handler = CommandHandler('start', start)
  dispatcher.add_handler(start_handler)
  # dispatcher.add_handler(MessageHandler(Filters.photo, test_))
# không biết người ta commndn gì

  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(unknown_handler)

  updater.start_polling()
  updater.idle()
# nguồn kham khảo : https://smartengines.com/building-an-ocr-bot-in-5-minutes-using-python/
if __name__ == '__main__':
    main()
