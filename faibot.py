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
        super().send_message(chat_id, text, parse_mode=self.mode)

    def send_me(self, text):
        self.send_message(self.my_id, text)

    def send_group(self, text):
        self.send_message(self.group_id, text)

    def check(self):
        self.send_me(message.datetime())

    def send_discussion(self, discussion):
        self.send_me(message.build(
            alias=discussion.subject.alias,
            notice=message.NOTICE_POST,
            title=discussion.title,
            url=discussion.url
        ))

    def send_url(self, url):
        self.send_group(message.build(
            alias=url.subject.alias,
            notice=message.identify_notice(url.path),
            title=url.name,
            url=url.path
        ))

    def send_photo(self, path):
        super().send_photo(self.group_id, photo=open(path, 'rb'))
