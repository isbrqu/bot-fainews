from orator import Model
from orator.orm import scope

class Thread(Model):

    __table__ = 'threads'
    __timestamps__ = False

    @scope
    def last_url(self, query, subject_id):
        return query.select('url').where('subject_id', subject_id).order_by('id', 'desc').first().url
