from scrapy import Spider
from pprint import pprint
from scrapy.loader import ItemLoader
from scrapy import Item
from scrapy import Field

class PedcoSpider(Spider):
    name = 'PedcoSpider'
    start_urls = ['https://pedco.uncoma.edu.ar/course/index.php']
    allowed_domains = ['pedco.uncoma.edu.ar']

    def parse(self, response):
        category_id = response.css('#page-navbar li:last-child')
        category_id = self._extract_id(category_id)
        subcategories = response.css('h3.categoryname')
        for subcategory in subcategories:
            yield {
                'id': self._extract_id(subcategory),
                'name': subcategory.css('a::text').get(),
                'category_id': category_id,
            }
        pagination = subcategories.css('a::attr(href)').getall()
        pagination = [f'{url}&perpage=200' for url in pagination]
        yield from response.follow_all(
            urls=pagination,
            callback=self.parse,
        )

    def _extract_id(self, selector):
        return selector.css('a::attr(href)').re_first('=(\d+)', 0)

