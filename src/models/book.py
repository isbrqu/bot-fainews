from orator import Model


class Book(Model):

    __table__ = 'books'
    __timestamps__ = True
    __primary_key__ = 'id'

