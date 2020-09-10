from decouple import config
from orator.orm import Model, accessor

URL_COURSE = config('URL_BASE') + 'course/view.php?id=%d'

class Course(Model):

    __table__ = 'materia'
    __timestamps__ = False
    __primary_key__ = 'idMateria'

    @accessor
    def url(self):
        return URL_COURSE % self.get_raw_attribute('numeroUrl')

    @classmethod
    def first_period(cls):
        return cls().new_query_without_scopes()\
            .where('cuatrimestre', 1)\
            .or_where('esRecursable', True)\
            .get()

    @classmethod
    def second_period(cls):
        return cls().new_query_without_scopes()\
            .where('cuatrimestre', 2)\
            .or_where('esRecursable', True)\
            .get()

