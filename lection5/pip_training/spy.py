from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def log_me(update: Update, context: CallbackContext):
    with open('users_log.csv', 'a', encoding='UTF8') as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')