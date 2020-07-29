#!python3
# -*- coding: utf-8 -*-

from time import ctime, sleep
from decouple import config

from pedco import Pedco
from faibot import Faibot

from models import Subject, Thread, BoardUrls

if __name__ == '__main__':

    bot = Faibot()
    pedco = Pedco()
    subjects = Subject.all()
    username = config('PEDCO_USERNAME')
    password = config('PEDCO_PASSWORD')

    while True:
        try:
            print('iniciando sesión...')
            while not pedco.login(username, password):
                print('no se pudo iniciar sesión')
                print('title:', pedco.title)
                sleep(120)
                print('iniciando sesión...')
            print('sesión inicianda')

            while pedco.logged_in:
                for subject in subjects:
                    pedco.subject = subject

                    pedco.go_course()
                    urls = BoardUrls.where('subject_id', subject.id).lists('url')
                    newurls = pedco.board.diffurl(urls)

                    if newurls:
                        BoardUrls.insert(newurls)
                        for url in newurls:
                            bot.send_url(subject.alias, url)
                        print(ctime(), '- link/s en', subject.name)

                    pedco.go_forum()
                    newthread = pedco.first_thread
                    if newthread.url != Thread.last_url(subjects.id):
                        Thread.insert(newthread.data)
                        bot.send_news(subject.alias, newthread.name, newthread.url)
                        pedco.go(newthread.url)
                        img = pedco.screenshot_article()
                        bot.send_photo(img)
                        print(ctime(), '- publicación en', subject.name)

                    print(ctime(), '- verificó', subject.name)

                bot.check()
                sleep(config('TIME_SLEEP', cast=int))
            print('la sesión expiró')
        except Exception as e:
            if config('DEBUG', default=True, cast=bool):
                raise e
            print(f'{ctime()} - {e}')
            sleep(120)
