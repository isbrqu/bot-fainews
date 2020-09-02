from decouple import config

DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': config('DB_HOST'),
        'database': config('DB_DATABASE'),
        'user': config('DB_USER'),
        'password': config('DB_PASSWORD'),
        'prefix': ''
    }
}

