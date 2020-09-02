from orator import Model


class Book(Model):

    __table__ = 'libro'
    __timestamps__ = False

