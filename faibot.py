import re
import telegram
from telegram.utils.helpers import escape_markdown
from datetime import datetime
from decouple import config
from functools import wraps

BASE = """
*Materia*: {course}\n
*Descripción*: {description}
{name}\n
_Link: {url}_
"""
DATETIME = '`%a %H:%M:%S`'

TOKEN = config('TELEGRAM_BOT_TOKEN')
PARSE_MODE = telegram.ParseMode.MARKDOWN_V2
MY_ID = config('TELEGRAM_MY_CHAT')
GROUP_ID = config('TELEGRAM_GROUP_CHAT')
if config('DEBUG', cast=bool):
    GROUP_ID = MY_ID

class Faibot(telegram.Bot):
    """docstring for Faibot"""
    def __init__(self):
        super().__init__(token=TOKEN)

    def __send_message(self, chat_id, text):
        super().send_message(chat_id, text, parse_mode=PARSE_MODE)

    def send_me(function):
        @wraps(function)
        def wrapper(self, *args):
            self.__send_message(MY_ID, function(self, *args))
        return wrapper

    def send_group(function):
        @wraps(function)
        def wrapper(self, *args):
            self.__send_message(GROUP_ID, function(self, *args))
        return wrapper

    @send_me
    def check(self):
        return datetime.now().strftime(DATETIME)

    @send_group
    def send_resource(self, resource):
        return BASE.format(
            course=self.__escape(resource.course),
            description=self.__escape(resource.msg),
            name=self.__escape(resource.name),
            url=self.__escape(resource.url)
        )

    def send_photo(self, path):
        super().send_photo(GROUP_ID, photo=open(path, 'rb'))

    def __escape(self, text):
        return escape_markdown(text, version=2)

