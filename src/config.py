from collections import namedtuple  
from os import getenv as env
import telegram as telegram_lib

DATABASES = {
    'mysql': {
        'database': env('DB_DATABASE'),
        'driver': env('DB_DRIVE'),
        'host': env('DB_HOST'),
        'password': env('DB_PASSWORD'),
        'prefix': '',
        'user': env('DB_USER'),
    }
}

DATABASE = DATABASES['mysql']

TELEGRAM = {
    'token': env('TELEGRAM_TOKEN'),
    'my_chat_id': env('TELEGRAM_MY_CHAT'),
    'group_chat_id': env('TELEGRAM_GROUP_CHAT'),
    'parse_mode': telegram_lib.ParseMode.MARKDOWN_V2,
}

DEBUG = {
    'active': True,
    'time_succesful': 10,
    'time_fail': 10,
}

DATETIME = {
    'format': '%a %h:%m:%s',
}

PAGE = {
    'cred_password': env('CRED_PASSWORD'),
    'cred_username': env('CRED_USERNAME'),
    'url_base': env('URL_BASE'),
    'url_login': env('URL_BASE') + env('URL_LOGIN'),
    'url_enrol': env('URL_BASE') + env('URL_ENROL'),
    'url_course': env('URL_BASE') + env('URL_COURSE'),
    'url_forum': env('URL_BASE') + env('URL_FORUM'),
    'title_login': env('TITLE_LOGIN'),
}

Database = namedtuple('Database', DATABASE.keys())
Telegram = namedtuple('Telegram', TELEGRAM.keys())
Debug = namedtuple('Debug', DEBUG.keys())
Datetime = namedtuple('Datetime', DATETIME.keys())
Page = namedtuple('Page', PAGE.keys())

telegram = Telegram(**TELEGRAM)
database = Database(**DATABASE)
debug = Debug(**DEBUG)
datatime = Datetime(**DATETIME)
page = Page(**PAGE)
