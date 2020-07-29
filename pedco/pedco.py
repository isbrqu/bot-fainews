from PIL import Image
from io import BytesIO
from datetime import datetime
from selenium import webdriver

from thread import Thread
from board import Board
from utils import URL_LOGIN, URL_MY, URL_COURSE, URL_FORUM
from message import TITLE_LOGIN

class Pedco:
    """docstring for Pedco"""
    def __init__(self, path):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1400, 1000)
        self.subject = None

    @property
    def in_login(self):
        return (self.driver.current_url == URL_LOGIN)

    @property
    def title(self):
        return self.driver.title

    def login(self, username=None, password=None):
        self.driver.get(URL_LOGIN)
        if username and password and self.title == TITLE_LOGIN:
            if not self.driver.find_elements_by_id('notice'):
                self.driver.find_element_by_name('username').send_keys(username)
                self.driver.find_element_by_name('password').send_keys(password)
                self.driver.find_element_by_id('loginbtn').click()
            else:
                self.my()
        return not self.in_login

    def my(self):
        self.driver.get(URL_MY)

    def go(self, url):
        self.driver.get(url)

    def go_course(self):
        self.driver.get(URL_COURSE % self.subject.course)

    def go_forum(self):
        self.driver.get(URL_FORUM % self.subject.forum)

    @property
    def board(self):
        return Board(self.driver.find_element_by_id('region-main'), self.subject.id)

    @property
    def first_thread(self):
        return Thread(self.driver.find_element_by_css_selector('tr.discussion'), self.subject.id)

    def screenshot_article(self):
        article = self.driver.find_element_by_tag_name('article')
        location, size = article.location, article.size
        img = Image.open(BytesIO(self.driver.get_screenshot_as_png()))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        img = img.crop((left, top, right, bottom))
        date_time = datetime.now().strftime('%m-%d-%H-%M-%S')
        path = f'img/{self.subject.name}-{date_time}.png'
        img.save(path)
        return path
