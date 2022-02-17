from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import requests
from spy import *


def hi_command(update: Update, context: CallbackContext):
    log_me(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_me(update: Update, context: CallbackContext):
    log_me(update, context)
    update.message.reply_text(f'/hi\n/USDrate\n')

def usd_rate(update: Update, context: CallbackContext):
    log_me(update, context)
    rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    update.message.reply_text(rate['Valute']['USD']['Value'])


