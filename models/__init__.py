# -*- coding: utf-8 -*-

from decouple import config
from orator import DatabaseManager, Model
from .subject import Subject
from .thread import Thread
from .board_urls import BoardUrls

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
