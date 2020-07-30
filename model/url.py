from orator import Model
from orator.orm import scope
from .url_category import UrlCategory

class Url(Model):

    __table__ = 'urls'
    __timestamps__ = False

    @scope
    def of_subject(self, query, subject):
        return query.where('subject_id', subject.id)

    @scope
    def insert_with_subject(self, query, urls, subject):
        categories = UrlCategory.lists('id', 'name')
        names = categories.keys()
        for url in urls:
            url['subject_id'] = subject.id
            url['url_category_id'] = 1
            for name in names:
                if name in url['url']:
                    url['url_category_id'] = categories[name]
                    break
        return query.insert(urls)
