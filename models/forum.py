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
    def first_period(cls):
        return cls().new_query_without_scopes()\
            .select('foro.*', 'materia.nombre as materia')\
            .join('materia', 'foro.idMateria', '=', 'materia.idMateria')\
            .where('materia.cuatrimestre', 1)\
            .or_where('materia.esRecursable', True)\
            .get()

    @classmethod
    def second_period(cls):
        return cls().new_query_without_scopes()\
            .select('foro.*', 'materia.nombre as materia')\
            .join('materia', 'foro.idMateria', '=', 'materia.idMateria')\
            .where('materia.cuatrimestre', 2)\
            .or_where('materia.esRecursable', True)\
            .get()


