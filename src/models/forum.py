from orator import Model


class Forum(Model):

    __table__ = 'forums'
    __timestamps__ = True
    __primary_key__ = 'id'

