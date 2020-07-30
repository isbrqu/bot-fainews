from orator import Model
from orator.orm import has_many
from .url import Url

class Subject(Model):

    __table__ = 'subjects'
    __timestamps__ = False

    @has_many
    def forums(self):
        return Url
