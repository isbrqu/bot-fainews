from datetime import datetime
from pprint import pprint
from scrapy import Spider
from urllib.parse import parse_qs
import urllib.parse as urlparse

now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

class Category(Spider):
    name = 'category'
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
        subcategories = response.css('h3.categoryname')
        category_id = self._param(response.url, 'categoryid')
        pagination = []
        for subcategory in subcategories:
            url = subcategory.css('a::attr(href)').get()
            pagination.append(f'{url}&perpage=200')
            yield {
                'id': self._param(url, 'categoryid') or '0',
                'name': subcategory.css('a::text').get().strip(),
                'category_id': category_id,
            }
        yield from response.follow_all(urls=pagination, callback=self.parse)

    def _param(self, url, param):
        parsed = urlparse.urlparse(url)
        _id = parse_qs(parsed.query).get(param, [''])[0]
        return _id


