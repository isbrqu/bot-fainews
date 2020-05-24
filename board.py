import re
from orator import Collection

YT = r'((?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))(?:[a-zA-Z0-9_-]{11})?)'

class Board:
	"""docstring for Board"""
	def __init__(self, element, subject_id):
		self.urls = extract_urls(element, subject_id)
		self.newurls = []

	def diffurl(self, urls):
		self.newurls = [url for url in self.urls if url['url'] not in urls]
		return self.newurls

    def extract_urls(self, element, subject_id):
        youtube = re.findall(YT, element.get_attribute('innerHTML'))
        urls = [{'name': 'Youtube video', 'url': url, 'subject_id': subject_id} for url in youtube]
        board = element.find_elements_by_tag_name('a')
        urls.extend([{'name': a.get_attribute('text'), 'url': a.get_attribute('href'), 'subject_id': subject_id}
            for a in board if 'youtu' not in a.get_attribute('href')
        ])
        urls = Collection(urls).unique('url').all()
        return urls
