import re
from orator import Collection

YT = r'((?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))(?:[a-zA-Z0-9_-]{11})?)'

class Board:
	"""docstring for Board"""
	def __init__(self, element, subject_id):
		youtube = re.findall(YT, element.get_attribute('innerHTML'))
		self.urls = [{'name': 'Youtube video', 'url': url, 'subject_id': subject_id} for url in youtube]
		board = element.find_elements_by_tag_name('a')
		self.urls.extend([{'name': a.get_attribute('text'), 'url': a.get_attribute('href'), 'subject_id': subject_id}
			for a in board if 'youtu' not in a.get_attribute('href')
		])
		self.urls = Collection(self.urls).unique('url').all()
		self.newurls = []

	def diffurl(self, urls):
		self.newurls = [url for url in self.urls if url['url'] not in urls]
		return self.newurls
