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
    def insert_with_subject(self, query, urls1, subject):
        urls2 = Url.where('subject_id', subject.id).lists('url')
        urls = urls1.filter(lambda item: item['url'] not in urls2).all()
        if urls:
            categories = UrlCategory.lists('id', 'name')
            categories_names = categories.keys()
            for url in urls:
                url['subject_id'] = subject.id
                url['url_category_id'] = 1
                for name in categories_names:
                    if name in url['url']:
                        url['url_category_id'] = categories[name]
                        break
            query.insert(urls)
        return query
