from orator import Model


class Chapter(Model):

    __table__ = 'capitulo'
    __timestamps__ = False
    __primary_key__ = 'idCapitulo'

