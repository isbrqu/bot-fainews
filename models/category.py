from orator import Model


class Category(Model):

    __table__ = 'categories'
    __timestamps__ = False
    __primary_key__ = 'id'
