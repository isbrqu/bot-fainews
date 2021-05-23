from orator import Model


class BoardUrl(Model):

    __table__ = 'board_urls'
    __timestamps__ = False
    __primary_key__ = 'id'
