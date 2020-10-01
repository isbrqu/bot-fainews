from decouple import config
from orator.orm import Model, accessor

URL_FORUM = config('URL_BASE') + 'mod/forum/view.php?id=%d'

class Forum(Model):

    __table__ = 'foro'
    __timestamps__ = False
    __primary_key__ = 'idForo'

    @accessor
    def url(self):
        return URL_FORUM % self.get_raw_attribute('numeroUrl')

    @classmethod
    def everyone_in_the_period(cls, period):
        return cls().new_query_without_scopes()\
            .select('foro.*', 'materia.alias as materia')\
            .join('materia', 'foro.idMateria', '=', 'materia.idMateria')\
            .where('materia.cuatrimestre', period)\
            .or_where('materia.esRecursable', True)\
            .get()

