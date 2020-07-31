#!python3
# -*- coding: utf-8 -*-
import time
from decouple import config

from pedco import Pedco
from faibot import Faibot

from model import Subject
from model import Discussion
from model import Url

if __name__ == '__main__':

    USERNAME = config('PEDCO_USERNAME')
    PASSWORD = config('PEDCO_PASSWORD')
    TIME_SLEEP_SUCCESFUL = config('TIME_SLEEP', cast=int)
    TIME_SLEEP_FAIL = config('TIME_SLEEP_FAIL', cast=int)
    DEBUG = config('DEBUG', default=True, cast=bool)

    bot = Faibot()
    pedco = Pedco()
    subjects = Subject.all()

    while True:
        try:
            print('iniciando sesión...')
            while not pedco.login(USERNAME, PASSWORD):
                print('no se pudo iniciar sesión')
                print('title:', pedco.title)
                time.sleep(TIME_SLEEP_FAIL)
                print('iniciando sesión...')
            print('sesión inicianda')
            while True:
                for subject in subjects:
                    pedco.open(subject.url)
                    urls = pedco.board.urls
                    Url.insert_with_subject(urls, subject)
                    for forum in subject.forums:
                        pedco.open(forum.url)
                        dis = pedco.last_discussion
                        if Discussion.is_new(dis):
                            pedco.open(dis.url)
                            dis.img = pedco.screenshot_discussion(subject.name)
                            Discussion.insert_with_subject(dis, subject)
                for url in Url.not_sent():
                    bot.send_url(url)
                    url.update_to_shipped()
                for dis in Discussion.not_sent():
                    bot.send_discussion(dis)
                    dis.update_to_shipped()
                bot.check()
                print('sleep...')
                time.sleep(TIME_SLEEP)
        except Exception as e:
            if DEBUG:
                raise e
            print(time.ctime(), e)
            time.sleep(TIME_SLEEP_FAIL)
