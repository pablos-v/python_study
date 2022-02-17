from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot import *



updater = Updater('5293815590:AAES4pa-TLVjgbu8zNp9fn6f19uboSJ1Lek')
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('USDrate', usd_rate))
updater.dispatcher.add_handler(CommandHandler('help', help_me))

print('started')
updater.start_polling()
updater.idle()
