# from decouple import config
import config
from mechanicalsoup import StatefulBrowser
from urllib.parse import parse_qs
import urllib.parse as urlparse

def _param(url, param):
    parsed = urlparse.urlparse(url)
    value = parse_qs(parsed.query).get(param)
    return value[0] if value else ''


class MechanicalMoodle(StatefulBrowser):

    def __init__(self):
        super().__init__()
        self.username = None
        self.password = None

    @property
    def in_login(self):
        return (self.url == config.page.url_login
            and self.page.title.text == config.page.title_login)

    @property
    def logged_in(self):
        return not self.in_login

    @property
    def sesskey(self):
        if not self._sesskey:
            a = self.page.select_one("a[href*='sesskey']")
            self._sesskey = _param(a.attrs.get('href'), 'sesskey')
        return self._sesskey

    def open(self, url):
        success = False
        while not success:
            try:
                super().open(url, timeout=5)
                success = True
            except Exception as e:
                print(e)
                time.sleep(2)
        return success

    def open_with_session(self, url):
        success = False
        while not success:
            if self.in_login:
                print('se ha cerrado la sesión')
                self.login()
            else:
                success = True
                self.open(url)
        return success

    def login(self, username=None, password=None):
        if not username and not password and self.username and self.password:
            username = self.username
            password = self.password
        else:
            raise Exception('Undefined username or password')
        self.open(config.page.url_login)
        if self.page.find('h4'):
            self.select_form(nr=1)
        else:
            self.select_form()
            self['username'] = username
            self['password'] = password
        self.submit_selected()
        return self.logged_in

