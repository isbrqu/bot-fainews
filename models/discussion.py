from orator import Model


class Discussion(Model):

    __table__ = 'discussions'
    __timestamps__ = True
    __primary_key__ = 'id'
