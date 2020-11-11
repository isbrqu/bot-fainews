import time

from decouple import config
from mechanicalsoup import StatefulBrowser

URL_LOGIN = config('URL_BASE') + 'login/index.php'
URL_HOME = config('URL_BASE') + '/my'
TITLE_LOGIN = 'PEDCO: Entrar al sitio'

class MechanicalMoodle(StatefulBrowser):

    def __init__(self):
        super().__init__()
        self.username = None
        self.password = None
        self.open(URL_HOME) 

    @property
    def page(self):
        return super().get_current_page()

    @property
    def url(self):
        return self.get_url()

    @property
    def title(self):
        return self.page.title.text

    @property
    def in_login(self):
        return (self.url == URL_LOGIN and self.title == TITLE_LOGIN)

    @property
    def logged_in(self):
        return (not self.in_login or self.page.find('h4'))

    def open(self, url):
        while True:
            try:
                super().open(url, timeout=5)
                return True
            except Exception as e:
                print(e)
                time.sleep(2)

    def login(self):
        if not self.logged_in:
            if not self.username or not self.password:
                raise Exception('Undefined username or password')
            self.select_form()
            self['username'] = self.username
            self['password'] = self.password
            self.submit_selected()
        return self.logged_in

    def open_with_session(self, url):
        if URL_LOGIN in url:
            url = URL_HOME
        self.open(url)
        while not self.logged_in:
            print('se cerró la sesión')
            self.login()
            self.open(url)
        return self.logged_in

