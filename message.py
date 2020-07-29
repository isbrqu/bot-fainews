import json
import re
from datetime import datetime as dt

MSG = json.load(open('messages.json', 'r', encoding='utf-8'))

BASE = MSG['base']
DATETIME = MSG['datetime']
NOTICES = MSG['notices']
TITLE_LOGIN = MSG['title_login']

NOTICE_POST = NOTICES['special']['post']
NOTICE_UNKNOW = NOTICES['special']['unknow']
NOTICES_NORMAL = NOTICES['normal']
NOTICES_NORMAL_LIST = NOTICES_NORMAL.keys()


def datetime():
    return dt.now().strftime(DATETIME)

def identify_notice_by_text(text):
    msg = NOTICE_UNKNOW
    for key in NOTICES_NORMAL_LIST:
        if key in text:
            msg = NOTICES_NORMAL[key]
            break
    return msg

def build(alias, notice, title, url):
    return BASE.format(
        alias=escape(alias),
        notice=escape(notice),
        title=escape(title),
        url=escape(url)
    )

def escape(text):
    return re.sub(r'([._*`{}\[\]()~>#|!?+=-])', r'\\\1', text)
