from config import DATABASES
from orator import DatabaseManager, Model
from .board_url import BoardUrl
from .book import Book
from .category import Category
from .chapter import Chapter
from .course import Course
from .discussion import Discussion
from .forum import Forum
from .user import User

Model.set_connection_resolver(DatabaseManager(DATABASES))

