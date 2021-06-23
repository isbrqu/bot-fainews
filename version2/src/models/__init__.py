from config import DATABASES
from orator import DatabaseManager, Model

Model.set_connection_resolver(DatabaseManager(DATABASES))

