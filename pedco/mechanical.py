import urlp
from mechanicalsoup import StatefulBrowser
from message import TITLE_LOGIN
from decouple import config

class Mechanical(StatefulBrowser):
    """docstring for Mechanical"""
    def __init__(self, subjects=[]):
        super().__init__()
        self.subjects = subjects
        self.forums = []
        self.discussions = []

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
        return (self.url == urlp.LOGIN)

    @property
    def logged_in(self):
        return not self.in_login

    def _update_courses(self):
        nav = self.page.select_one('#nav-drawer')
        links = nav.find_all('a', {'data-parent-key': 'mycourses'})
        self.subjects = []
        for a in links:
            self.subjects.append({
                'name': a.text.replace('\n', '').lower(),
                'url': a['href']
            })

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
                self.loginenv()
            else:
                success = True
                self.open(url)
        return success

    def login(self, username, password):
        self.open(urlp.LOGIN)
        if self.page.find('h4'):
            self.select_form(nr=1)
        else:
            self.select_form()
            self['username'] = username
            self['password'] = password
        self.submit_selected()
        success = self.logged_in
        if success and not self.courses:
            self._update_courses()
        return success
