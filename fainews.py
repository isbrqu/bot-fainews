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
                print('UPDATING RESOURCES')
                mechanical.update_resources()
                for new in mechanical.resources_not_sent:
                    bot.send_resource(new)
                    new.enviado = True
                    new.save()
                print('UPDATING DISCUSSIONS')
                mechanical.update_discussions()
                for new in mechanical.discussions_not_sent:
                    bot.send_discussions(new)
                    new.enviado = True
                    new.save()
                bot.check()
                raise Exception('good!')
                morfeo.succesful('a mimir...')
        except Exception as e:
            if DEBUG:
                raise e
            morfeo.fail(e)

