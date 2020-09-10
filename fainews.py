#!python3
# -*- coding: utf-8 -*-
import time
from decouple import config

from pedco import Mechanical
from faibot import Faibot

if __name__ == '__main__':

    USERNAME = config('PEDCO_USERNAME')
    PASSWORD = config('PEDCO_PASSWORD')
    TIME_SLEEP_SUCCESFUL = config('TIME_SLEEP', cast=int)
    TIME_SLEEP_FAIL = config('TIME_SLEEP_FAIL', cast=int)
    DEBUG = config('DEBUG', default=True, cast=bool)

    bot = Faibot()
    mechanical = Mechanical()

    while True:
        try:
            print('iniciando sesión...')
            while not mechanical.login(USERNAME, PASSWORD):
                print('no se pudo iniciar sesión')
                print('title:', mechanical.title)
                time.sleep(TIME_SLEEP_FAIL)
                print('iniciando sesión...')
            print('sesión inicianda')
            while True:
                mechanical.update_resources()
                for new in mechanical.new_resources:
                    bot.send_resource(new)
                    print(f'{new.course} --> {new.typer} --> {new.name}')
                    new.enviado = True
                    new.save()
                bot.check()
                print('a mimir...')
                time.sleep(TIME_SLEEP_SUCCESFUL)
        except Exception as e:
            if DEBUG:
                raise e
            print(time.ctime(), e)
            time.sleep(TIME_SLEEP_FAIL)

