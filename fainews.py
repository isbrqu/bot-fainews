#!python3
# -*- coding: utf-8 -*-

from time import ctime, sleep
from decouple import config
from colorama import Fore, init
from orator import DatabaseManager, Model

from pedco import Pedco
from faibot import Faibot

from models import Subject
from models import Thread
from models import BoardUrls

if __name__ == '__main__':
    
    init(convert=True, autoreset=True)
    Model.set_connection_resolver(DatabaseManager({
        'mysql': {
            'driver':   'mysql',
            'host':     config('DB_HOST'),
            'database': config('DB_DATABASE'),
            'user':     config('DB_USER'),
            'password': config('DB_PASSWORD'),
            'prefix':   '',
        }
    }))
    bot = Faibot()
    pedco = Pedco()
    subjects = Subject.all()

    while True:
        try:
            print('iniciando sesión...')
            while not pedco.login(username=config('PEDCO_USERNAME'), password=config('PEDCO_PASSWORD')):
                print(Fore.RED + 'no se pudo iniciar sesión')
                print('title: ' + pedco.get_title())
                sleep(120)
                print('iniciando sesión...')
            print('sesión inicianda')

            while not pedco.in_login():
                for subject in subjects:
                    pedco.subject_id = subject.id

                    pedco.go(subject.course)
                    board = pedco.get_board()
                    urls = BoardUrls.where('subject_id', subject.id).lists('url')
                    newurls = board.diffurl(urls)

                    if newurls:
                        BoardUrls.insert(newurls)
                        for url in newurls:
                            bot.send_url(subject.alias, url)
                        print(Fore.GREEN + ctime() + ' - link/s en ' + subject.name)

                    pedco.go(subject.forum)
                    newthread = pedco.get_first_thread()
                    oldthread = Thread.select('url').where('subject_id', subject.id).order_by('id', 'desc').first()

                    if not oldthread or newthread.url != oldthread.url:
                        Thread.insert(newthread.get_data())
                        bot.send_nov(subject.alias, newthread.name, newthread.url)
                        pedco.go(newthread.url)
                        img = pedco.screenshot_article(subject.name)
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
