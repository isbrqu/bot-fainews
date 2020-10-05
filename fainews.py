#!python3
# -*- coding: utf-8 -*-
import time
import morfeo
import bot
from decouple import config

from pedco import MechanicalPedco

if __name__ == '__main__':

    pedco = PedcoBrowser()
    pedco.username = config('PEDCO_USERNAME')
    pedco.password = config('PEDCO_PASSWORD')

    DEBUG = config('DEBUG', cast=bool)

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
                pedco.update_resources()
                print('UPDATING DISCUSSIONS')
                pedco.update_discussions()
                bot.check()
                raise Exception('good!')
                morfeo.succesful('a mimir...')
        except Exception as e:
            if DEBUG:
                raise e
            morfeo.fail(e)

