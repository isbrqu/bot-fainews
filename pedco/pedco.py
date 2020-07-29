from PIL import Image
from io import BytesIO
from datetime import datetime
from selenium import webdriver

import urlp
from thread import Thread
from board import Board
from message import TITLE_LOGIN

class Pedco(webdriver.PhantomJS):
    """docstring for Pedco"""
    def __init__(self, path):
        self.set_window_size(1400, 1000)
        self.subject = None

    @property
    def in_login(self):
        return (self.current_url == urlp.LOGIN)

    def login(self, username=None, password=None):
        self.get(urlp.LOGIN)
        if username and password and self.title == TITLE_LOGIN:
            if not self.find_elements_by_id('notice'):
                self.find_element_by_name('username').send_keys(username)
                self.find_element_by_name('password').send_keys(password)
                self.find_element_by_id('loginbtn').click()
            else:
                self.my()
        return not self.in_login

    def my(self):
        self.get(urlp.MY)

    def go(self, url):
        self.get(url)

    def go_course(self):
        self.get(urlp.COURSE % self.subject.course)

    def go_forum(self):
        self.get(urlp.FORUM % self.subject.forum)

    @property
    def board(self):
        return Board(self.find_element_by_id('region-main'), self.subject.id)

    @property
    def first_thread(self):
        return Thread(self.find_element_by_css_selector('tr.discussion'), self.subject.id)

    def screenshot_article(self):
        article = self.find_element_by_tag_name('article')
        location, size = article.location, article.size
        img = Image.open(BytesIO(self.get_screenshot_as_png()))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        img = img.crop((left, top, right, bottom))
        date_time = datetime.now().strftime('%m-%d-%H-%M-%S')
        path = f'img/{self.subject.name}-{date_time}.png'
        img.save(path)
        return path
