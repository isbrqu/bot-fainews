#!python3
# -*- coding: utf-8 -*-
import config
import morfeo
import time

from pedco import MechanicalPedco
from faibot import Faibot

def fail(msg=None):
    end = '->\n' if msg else ''
    print(time.ctime(), end=end)
    print(msg or '')
    time.sleep(config.debug.time_fail)

def succesful(msg=None):
    if msg:
        print(msg)
    time.sleep(config.debug.time_succesful)

if __name__ == '__main__':

    bot = Faibot()
    mechanical = MechanicalPedco()
    mechanical.username = config.page.cred_username
    mechanical.password = config.page.cred_password

    while True:
        try:
            print('iniciando sesión...')
            while not mechanical.login():
                print('no se pudo iniciar sesión')
                fail(f'title: {mechanical.title}')
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
                succesful('a mimir...')
        except Exception as e:
            if DEBUG:
                raise e
            fail(e)

