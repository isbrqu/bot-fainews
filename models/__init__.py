from decouple import config
from orator import DatabaseManager, Model

from .book import Book
from .chapter import Chapter
from .course import Course
from .forum import Forum
from .resource import Resource
from .type_resource import TypeResource
from .discussion import Discussion

Model.set_connection_resolver(DatabaseManager({
    'mysql': {
        'driver': 'mysql',
        'host': config('DB_HOST'),
        'database': config('DB_DATABASE'),
        'user': config('DB_USER'),
        'password': config('DB_PASSWORD'),
        'prefix': '',
    }
}))

