import re
import telegram
from datetime import datetime
from decouple import config

BASE = """
*Materia*: {course}\n
*Descripción*: {description}
{name}\n
_Link: {url}_
"""

DATETIME = '`%a %H:%M:%S`'

class Faibot(telegram.Bot):
    """docstring for Faibot"""
    def __init__(self):
        super().__init__(token=config('TELEGRAM_BOT_TOKEN'))
        self.mode = telegram.ParseMode.MARKDOWN_V2
        self.my_id = config('TELEGRAM_MY_CHAT')
        self.group_id = config('TELEGRAM_GROUP_CHAT')
        self.debug = config('DEBUG', default=True, cast=bool)
        if self.debug:
            self.group_id = self.my_id

    def send_message(self, chat_id, text):
        super().send_message(chat_id, text, parse_mode=self.mode)

    def send_me(self, text):
        self.send_message(self.my_id, text)

    def send_group(self, text):
        self.send_message(self.group_id, text)

    def check(self):
        self.send_me(datetime.now().strftime(DATETIME))

    def send_resource(self, resource):
        self.send_group(self._build(
            course=resource.course,
            description=resource.msg,
            name=resource.name,
            url=resource.url
        ))

    def send_photo(self, path):
        super().send_photo(self.group_id, photo=open(path, 'rb'))

    def _build(self, course, description, name, url):
        return BASE.format(
            course=self._escape(course),
            description=self._escape(description),
            name=self._escape(name),
            url=self._escape(url)
        )

    def _escape(self, text):
        return re.sub(r'([._*`{}\[\]()~>#|!?+=-])', r'\\\1', text)

