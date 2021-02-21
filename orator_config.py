from decouple import config

DATABASES = {
    'mysql': {
        'database': config('DB_DATABASE'),
        'driver': config('DB_DRIVE'),
        'host': config('DB_HOST'),
        'password': config('DB_PASSWORD'),
        'prefix': '',
        'user': config('DB_USER'),
    }
}

