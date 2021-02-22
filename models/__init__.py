from orator import DatabaseManager, Model
from orator_config import DATABASES

from .book import Book
from .chapter import Chapter
from .course import Course
from .forum import Forum
from .resource import Resource
from .type_resource import TypeResource

Model.set_connection_resolver(DatabaseManager(DATABASES))

