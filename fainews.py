#!python3
# -*- coding: utf-8 -*-
import time
import morfeo
from decouple import config

from pedco import MechanicalPedco
from faibot import Faibot

if __name__ == '__main__':

    bot = Faibot()
    mechanical = MechanicalPedco()
    mechanical.username = config('PEDCO_USERNAME')
    mechanical.password = config('PEDCO_PASSWORD')

    DEBUG = config('DEBUG', default=True, cast=bool)

    while True:
        try:
            print('iniciando sesión...')
            while not mechanical.login():
                print('no se pudo iniciar sesión')
                morfeo.fail(f'title: {mechanical.title}')
                print('iniciando sesión...')
            print('sesión inicianda')
            while True:
                mechanical.update_resources()
                for new in mechanical.new_resources:
                    bot.send_resource(new)
                    print(f'{new.course} --> {new.typer} --> {new.name}')
                    new.enviado = True
                    new.save()
                mechanical.update_discussions()
                for new in mechanical.new_discussions:
                    bot.send_discussions(new)
                    print(f'{new.course} --> {new.forum} --> {new.name}')
                    new.enviado = True
                    new.save()
                bot.check()
                raise Exception('good!')
                morfeo.succesful('a mimir...')
        except Exception as e:
            if DEBUG:
                raise e
            morfeo.fail(e)

