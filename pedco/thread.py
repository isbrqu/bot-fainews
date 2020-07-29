import re

class Thread:
    """docstring for Thread"""
    def __init__(self, element, subject_id):
        td = element.find_elements_by_tag_name('td')
        a = td[1].find_element_by_tag_name('a')
        self.url = a.get_attribute('href')
        self.name = a.get_attribute('text')
        self.author = re.sub(r'\s{2,}', '', td[2].find_element_by_css_selector('div div.align-middle.p-2').get_attribute('innerHTML'))
        n = 4 if len(td) < 9 else 5
        a = td[n].find_elements_by_tag_name('a')
        self.last_to_write = a[1].get_attribute('text')
        self.updated = a[2].get_attribute('text')
        self.created = re.sub(r'\s{2,}', '', td[n+1].get_attribute('innerHTML'))
        self.subject_id = subject_id

    @property
    def data(self):
        return {
            'name': self.name,
            'url': self.url,
            'author': self.author,
            'last_to_write': self.last_to_write,
            'created': self.created,
            'updated': self.updated,
            'subject_id': self.subject_id
        }

    def __repr__(self):
        return f'url: {self.url}, name: {self.name}, author: {self.author}, created: {self.created}, last_to_write: {self.last_to_write}, updated: {self.updated}'
