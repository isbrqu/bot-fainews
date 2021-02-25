from datetime import datetime
from pprint import pprint
from scrapy import Spider
from urllib.parse import parse_qs
import urllib.parse as urlparse

now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

class Course(Spider):
    name = 'course'
    start_urls = ['https://pedco.uncoma.edu.ar/course/index.php']
    allowed_domains = ['pedco.uncoma.edu.ar']
    custom_settings = {
        'FEEDS': {
            f'csv/{name}-{now}.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': ['id', 'name', 'category_id'],
            }
        },
        'LOG_FILE': f'log/{name}.log',
        # 'CLOSESPIDER_PAGECOUNT': 10,
    }

    def parse(self, response):
        courses = response.css('.coursename')
        category_id = self._param(response.url, 'categoryid')
        for course in courses:
            url = course.css('a::attr(href)').get()
            yield {
                'id': self._param(url, 'id') or '0',
                'name': course.css('a::text').get().strip(),
                'category_id': category_id,
            } 
        subcategories = response.css('h3.categoryname')
        pagination = subcategories.css('a::attr(href)').getall()
        pagination = [f'{url}&perpage=200' for url in pagination]
        yield from response.follow_all(urls=pagination, callback=self.parse)

    def _param(self, url, param):
        parsed = urlparse.urlparse(url)
        _id = parse_qs(parsed.query).get(param, [''])[0]
        return _id

