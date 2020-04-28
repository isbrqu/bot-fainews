from PIL import Image
from io import BytesIO
from datetime import datetime
from selenium import webdriver

from thread import Thread
from board import Board

URL_LOGIN = 'https://pedco.uncoma.edu.ar/login/index.php'
URL_MY = 'https://pedco.uncoma.edu.ar/my/'

class Pedco:
    """docstring for Pedco"""
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1400,1000)

    def login(self, username=None, password=None):
        self.driver.get(URL_LOGIN)
        if username and password and self.driver.title == 'PEDCO: Entrar al sitio':
            if not self.driver.find_elements_by_id('notice'):
                self.driver.find_element_by_name('username').send_keys(username)
                self.driver.find_element_by_name('password').send_keys(password)
                self.driver.find_element_by_id('loginbtn').click()
            else:
                self.my()
        return not self.in_login()

    def my(self):
        self.driver.get(URL_MY)
        return self.in_login()

    def go(self, url):
        self.driver.get(url)
        return self.in_login()

    def in_login(self):
        return (self.driver.current_url == URL_LOGIN)

    def get_title(self):
        return self.driver.title

    def get_board(self):
        return Board(self.driver.find_element_by_id('region-main'))

    def get_first_thread(self):
        return Thread(self.driver.find_element_by_css_selector('tr.discussion'))

    def screenshot_article(self, name):
        article = self.driver.find_element_by_tag_name('article')
        location, size = article.location, article.size
        img = Image.open(BytesIO(self.driver.get_screenshot_as_png()))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        img = img.crop((left, top, right, bottom))
        date_time = datetime.now().strftime('%m-%d-%H-%M-%S')
        path = f'img/{name}-{date_time}.png'
        img.save(path)
        return path
