from orator import Model


class Forum(Model):

    __table__ = 'foro'
    __timestamps__ = False
    __primary_key__ = 'idForo'

