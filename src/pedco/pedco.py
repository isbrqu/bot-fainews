from PIL import Image
from io import BytesIO
from datetime import datetime
from selenium import webdriver

from .board import Board
from .discussion import Discussion
from message import TITLE_LOGIN

URL_MY =  'https://pedco.uncoma.edu.ar/my'

class Pedco(webdriver.PhantomJS):
    """docstring for Pedco"""
    def __init__(self):
        super().__init__()
        self.set_window_size(1400, 1000)
        self.subject = None

    @property
    def in_login(self):
        return (self.current_url == urlp.LOGIN and self.title == TITLE_LOGIN)

    @property
    def logged_in(self):
        return not self.in_login

    @property
    def board(self):
        return Board(self.find_element_by_id('region-main'))

    @property
    def first_thread(self):
        return Discussion(self.find_element_by_css_selector('tr.discussion'))

    def login(self, username, password):
        self.get(urlp.LOGIN)
        if self.in_login:
            if not self.find_elements_by_id('notice'):
                self.find_element_by_name('username').send_keys(username)
                self.find_element_by_name('password').send_keys(password)
                self.find_element_by_id('loginbtn').click()
            else:
                self.my()
        return not self.in_login

    def my(self):
        self.get(URL_MY)

    def screenshot_article(self, name):
        article = self.find_element_by_tag_name('article')
        location, size = article.location, article.size
        img = Image.open(BytesIO(self.get_screenshot_as_png()))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        img = img.crop((left, top, right, bottom))
        dt = datetime.now().strftime('%m-%d-%H-%M-%S')
        path = f'img/{name}-{dt}.png'
        img.save(path)
        return path
