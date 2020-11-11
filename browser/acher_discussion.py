import re
from decouple import config

URL_FORUM = config('URL_BASE') + 'mod/forum/view.php?id=%d'

def clear_space(tag):
    return re.sub(r'\s{2,}|\n', '', tag.text)

class Discussion:
    
    def __init__(self, tr):
        self.td = tr.select('td')
        self._url_id = None
        self._name = None
        self._author = None
        self._created = None
        self._updated = None
        self._url = None

    @property
    def url_id(self):
        if not self._url_id:
            self._url_id = int(self.td[1].select_one('a')['href'].split('=')[1])
        return self._url_id

    @property
    def name(self):
        if not self._name:
            self._name = clear_space(self.td[1])
        return self._name

    @property
    def author(self):
        if not self._author:
            self._author = clear_space(self.td[2])
        return self._author

    @property
    def created(self):
        if not self._created:
            self._created = clear_space(self.td[-3])
        return self._created

    @property
    def updated(self):
        if not self._updated:
            self._updated = clear_space(self.td[-4].select('a')[2])
        return self._updated

    @property
    def url(self):
        if not self._url:
            self._url = URL_FORUM % self._url_id
        return self._url
        

