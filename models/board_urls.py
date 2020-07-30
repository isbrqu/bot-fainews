from orator import Model

class BoardUrls(Model):

    __table__ = 'board_urls'
    __timestamps__ = False

    @scope
    def of_subject(self, query, subject):
        return query.where('subject_id', subject.id)
