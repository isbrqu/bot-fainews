#!python3
# -*- coding: utf-8 -*-

from time import ctime, sleep
from decouple import config
from colorama import Fore, init

from pedco import Pedco
from faibot import Faibot
from subject import Subject

init(convert=True, autoreset=True)

SUBJECT = [
    Subject('calculo',     alias='Cálculo',     course='1891', forum='89531'),
    Subject('estructuras', alias='Estructuras', course='241', forum='13023'),
    Subject('ingles',      alias='Inglés',      course='665', forum='22060'),
    Subject('computacion', alias='TC I',        course='1865', forum='88332'),
    Subject('objetos',     alias='POO',         course='246', forum='197066'),
]

if __name__ == '__main__':
    bot = Faibot()
    pedco = Pedco()
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
                for subject in SUBJECT:
                    
                    pedco.go(subject.course)
                    board = pedco.get_board()
                    
                    with open(f'records/{subject.name}.urls', encoding='utf-8', mode='r+') as urls:
                        newurls = board.diffurl(urls.read().splitlines())
                        if newurls:
                            urls.writelines(newurls)
                            for url in board.newurls:
                                bot.send_url(subject.alias, url)

                    pedco.go(subject.forum)
                    thread = pedco.get_first_thread()
                    newline = f'{thread.name} - {thread.url}'

                    with open(f'records/{subject.name}.log', encoding='utf-8', mode='r+') as log:
                        oldline = log.readline().rstrip('\r\n')
                        if newline != oldline:
                            log.seek(0)
                            content = log.read()
                            log.seek(0)
                            log.write(newline.rstrip('\r\n') + '\n' + content)
                            bot.send_nov(subject.alias, thread.name, thread.url)
                            pedco.go(thread.url)
                            bot.send_photo(pedco.screenshot_article(subject.name))
                            print(Fore.GREEN + ctime() + ' - novedad en ' + subject.name)
                        else:
                            print(ctime() + ' - nada nuevo en ' + subject.name)

                bot.check()
                sleep(1800)
            print(Fore.YELLOW + 'la sesión expiró')
        except Exception as e:
            # raise e
            print(Fore.RED + f'{ctime()} - {e}')
            sleep(120)
