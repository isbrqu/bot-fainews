#!python3
# -*- coding: utf-8 -*-

from time import ctime, sleep
from decouple import config
from colorama import Fore, init

from pedco import Pedco
from faibot import Faibot

from models import Subject
from models import Thread
from models import BoardUrls

if __name__ == '__main__':
    
    init(convert=True, autoreset=True)

    bot = Faibot()
    pedco = Pedco()
    subjects = Subject.all()

    while True:
        try:
            print('iniciando sesión...')
            while not pedco.login(username=config('PEDCO_USERNAME'), password=config('PEDCO_PASSWORD')):
                print(Fore.RED + 'no se pudo iniciar sesión')
                print('title: ' + pedco.title)
                sleep(120)
                print('iniciando sesión...')
            print('sesión inicianda')

            while not pedco.in_login():
                for subject in subjects:
                    pedco.subject = subject

                    pedco.go_course()
                    board = pedco.board
                    urls = BoardUrls.where('subject_id', subject.id).lists('url')
                    newurls = board.diffurl(urls)

                    if newurls:
                        BoardUrls.insert(newurls)
                        for url in newurls:
                            bot.send_url(subject.alias, url)
                        print(Fore.GREEN + ctime() + ' - link/s en ' + subject.name)

                    pedco.go_forum()
                    newthread = pedco.first_thread
                    if newthread.url != Thread.last_url(subjects.id):
                        Thread.insert(newthread.data)
                        bot.send_nov(subject.alias, newthread.name, newthread.url)
                        pedco.go(newthread.url)
                        img = pedco.screenshot_article()
                        bot.send_photo(img)
                        print(Fore.GREEN + ctime() + ' - publicación en ' + subject.name)

                    print(ctime() + ' - verificó ' + subject.name)

                bot.check()
                sleep(config('TIME_SLEEP', cast=int))
            print(Fore.YELLOW + 'la sesión expiró')
        except Exception as e:
            if config('DEBUG', default=True, cast=bool):
                raise e
            print(Fore.RED + f'{ctime()} - {e}')
            sleep(120)
