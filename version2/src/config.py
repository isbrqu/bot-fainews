from collections import namedtuple  
from os import getenv as env
import telegram as telegram_lib

TELEGRAM = {
    'parse_mode': telegram_lib.ParseMode.MARKDOWN_V2,
    'token': env('TELEGRAM_TOKEN'),
    'id': env('TELEGRAM_ID'),
}

MOODLE = {
    'url': env('MOODLE_URL'),
    'token': env('MOODLE_TOKEN'),
}

telegram = namedtuple('Telegram', TELEGRAM.keys())(**TELEGRAM)
moodle = namedtuple('Moodle', MOODLE.keys())(**MOODLE)

