from orator import Model


class User(Model):

    __table__ = 'users'
    __timestamps__ = False
    __primary_key__ = 'id'
