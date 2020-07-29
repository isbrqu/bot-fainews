import telegram
import message
from decouple import config

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
        super().send_message(chat_id=chat_id, text=text, parse_mode=self.mode)

    def send_me(self, text):
        self.send_message(self.my_id, text)

    def send_group(self, text):
        self.send_message(self.group_id, text)

    def check(self):
        self.send_me(message.datetime())

    def send_news(self, alias, title, url):
        self.send_me(message.build(
            alias=alias,
            notice=message.NOTICE_POST,
            title=title,
            url=url
        ))

    def send_url(self, alias, url):
        self.send_group(message.build(
            alias=alias,
            notice=message.identify_notice_by_text(url['url']),
            title=url['name'],
            url=url['url']
        ))

    def send_photo(self, path):
        super().send_photo(chat_id=self.group_id, photo=open(path, 'rb'))
