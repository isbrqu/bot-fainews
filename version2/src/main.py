from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from moodleapi import Moodle
from time import sleep
import config

moodle = Moodle(config.moodle.url, token=config.moodle.token)
updater = Updater(config.telegram.token)

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def xd(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'XD\n*dubstep*')

def tequiero(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'y yo a ti <3')
    sleep(3)
    update.message.reply_text(f'...pero como amigo uwu')

def info(update: Update, context: CallbackContext) -> None:
    info = moodle.info
    if int(config.telegram.id) == update.effective_user.id:
        msg = f'Your name is {info.firstname}, your last name is {info.lastname} with username {info.username} and userid {info.userid}'
    else:
        msg = 'qué haces master? esta funcionalidad no está disponible para vos'
    update.message.reply_text(msg)

# alias of info
def whoami(update: Update, context: CallbackContext) -> None:
    info(update, context)

def courses(update: Update, context: CallbackContext) -> None:
    keys = {'id': 'id', 'shortname': 'alias', 'fullname': 'nombre'}
    msg = ''
    for course in moodle.courses:
        for key, name in keys.items():
            msg += f'{name}: {course[key]}\n'
        msg += '\n'
    update.message.reply_text(msg)

def helpp(update: Update, context: CallbackContext) -> None:
    msg = '/help, /whoiam and /hello'
    update.message.reply_text(msg)

functions = {
    'hello': hello,
    'help': helpp,
    'whoami': whoami,
    'info': info,
    'tequiero': tequiero,
    'courses': courses,
    'xd': xd,
}

for name, function in functions.items():
    updater.dispatcher.add_handler(CommandHandler(name, function))
updater.start_polling()
updater.idle()

