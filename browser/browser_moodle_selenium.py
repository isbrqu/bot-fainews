import time
from decouple import config
from selenium import webdriver

URL_LOGIN = config('URL_BASE') + 'login/index.php'
URL_HOME = config('URL_BASE') + 'my'
TITLE_LOGIN = 'PEDCO: Entrar al sitio'

class SeleniumMoodle(webdriver.PhantomJS):

    def __init__(self):
        super().__init__()
        self.set_window_size(1400, 1000)
        self.username = None
        self.password = None
        self.get(URL_HOME)
        print('title', super().current_url)

    @property
    def in_login(self):
        return (self.current_url == URL_LOGIN and self.title == TITLE_LOGIN)

    @property
    def logged_in(self):
        return (not self.in_login and self.find_elements_by_id('notice'))
    
    def get(sefl, url):
        while True:
            try:
                super().get(url)
                return True
            except Exception as e:
                print(e)
                time.sleep(2)

    def login(self):
        if not self.logged_in:
            if not self.username or not self.password:
                raise Exception('Undefined username or password')
            self.find_element_by_name('username').send_keys(self.username)
            self.find_element_by_name('password').send_keys(self.password)
            self.find_element_by_id('loginbtn').click()
        return self.logged_in

    def open_with_session(self, url):
        if URL_LOGIN in url:
            url = URL_HOME
        self.get(url)
        while not self.logged_in:
            print('se cerró la sesión')
            self.login()
            self.get(url)
        return self.logged_in

