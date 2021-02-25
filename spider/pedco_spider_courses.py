from scrapy import Spider
from pprint import pprint
import urllib.parse as urlparse
from urllib.parse import parse_qs
from datetime import datetime

now = datetime.now().strftime('%H-%M-%S-%Y')

class PedcoCourseSpider(Spider):
    name = 'PedcoSpider'
    start_urls = ['https://pedco.uncoma.edu.ar/course/index.php']
    allowed_domains = ['pedco.uncoma.edu.ar']
    custom_settings = {
        'FEEDS': {
            f'csv/courses-{now}.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': ['id', 'name', 'category_id'],
            }
        },
        'LOG_FILE': 'courses.log',
        'CLOSESPIDER_PAGECOUNT': 10,
    }

    def parse(self, response):
        courses = response.css('.coursename')
        category_id = self._param(response.url, 'categoryid')
        for course in courses:
            yield {
                'id': self._param(course.css('a::attr(href)').get(), 'id'),
                'name': course.css('a::text').get().strip(),
                'category_id': category_id,
            } 
        subcategories = response.css('h3.categoryname')
        pagination = subcategories.css('a::attr(href)').getall()
        pagination = [f'{url}&perpage=200' for url in pagination]
        yield from response.follow_all(pagination, self.parse)

    def _param(self, url, param):
        parsed = urlparse.urlparse(url)
        _id = parse_qs(parsed.query).get(param, [''])[0]
        return _id

