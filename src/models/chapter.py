from orator import Model


class Chapter(Model):

    __table__ = 'chapters'
    __timestamps__ = False
    __primary_key__ = 'id'

