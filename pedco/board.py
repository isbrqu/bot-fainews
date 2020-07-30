import re
from orator import Collection

YT = r'((?:https?:\/\/)?\
    (?:www\.)?\
    (?:youtu\.be|youtube\.com)\/\
    (?:embed\/|v\/|watch\?v=|watch\?.+&v=)\
    (?:[a-zA-Z0-9_-]{11}))'

class Board:
    """docstring for Board"""
    def __init__(self, element):
        self.urls = extract_urls(element)
        self.newurls = []

    def diffurl(self, urls):
        self.newurls = [url for url in self.urls if url['url'] not in urls]
        return self.newurls

    def extract_urls(self, element):
        for url in re.findall(YT, element.get_attribute('innerHTML')):
            urls.append({'name': 'Youtube video', 'url': url})
        for a in element.find_elements_by_tag_name('a'):
            urls.append({
                'name': a.get_attribute('text'),
                'url': a.get_attribute('href')
            })
        return Collection(urls).unique('url').all()
