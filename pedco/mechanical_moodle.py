import time
from decouple import config
from mechanicalsoup import StatefulBrowser

URL_LOGIN = config('URL_BASE') + 'login/index.php'
TITLE_LOGIN = 'PEDCO: Entrar al sitio'

class MechanicalMoodle(StatefulBrowser):

    def __init__(self):
        super().__init__()
        self.username = None
        self.password = None

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
        return not self.in_login

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
        self.open(URL_LOGIN)
        if self.page.find('h4'):
            self.select_form(nr=1)
        else:
            self.select_form()
            self['username'] = username
            self['password'] = password
        self.submit_selected()
        return self.logged_in

