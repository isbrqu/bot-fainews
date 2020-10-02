from decouple import config
from orator.orm import Model, accessor, scope

URL_DISCUSSION = config('URL_BASE') + 'mod/forum/discuss.php?d=%d'

class Discussion(Model):
 
    __table__ = 'discusion'
    __timestamps__ = False
    __primary_key__ = 'idDiscusion'

    @accessor
    def url(self):
        return URL_DISCUSSION  % self.get_raw_attribute('numeroUrl')

    @scope
    def with_url_id(self, query, url_id):
        return query.where('numeroUrl', url_id)

    @scope
    def joinForum(self, query):
        return query.join('foro', 'discusion.idForo', '=', 'foro.idForo')

    @scope
    def joinCourse(self, query):
        return query.join('materia', 'foro.idMateria', '=', 'materia.idMateria')

    @scope
    def not_sent(self, query):
        return query.where('enviado', False)

    @scope
    def sort(self, query):
        return query\
            .order_by('foro.idMateria')\
            .order_by('discusion.idDiscusion')\

