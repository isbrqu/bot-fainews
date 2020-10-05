from .telegram_bot import TelegramBot
from bot import TelegramBot
from pedco import PedcoReader

telegram_bot = TelegramBot()
pedco = PedcoReader()

while True:
    for new in pedco.resources_not_sent:
        telegram_bot.send_resource(new)
        new.enviado = True
        new.save()
    for new in pedco.discussions_not_sent:
        telegram_bot.send_discussions(new)
        new.enviado = True
        new.save()

