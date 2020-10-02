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

