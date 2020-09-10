from decouple import config
from orator import Model

URL_FORUM = config('URL_BASE') + 'mod/forum/view.php?id=%d'

class Forum(Model):

    __table__ = 'foro'
    __timestamps__ = False
    __primary_key__ = 'idForo'

