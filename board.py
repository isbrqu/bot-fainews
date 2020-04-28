import re

YT = r'((?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))(?:[a-zA-Z0-9_-]{11})?)'

class Board:
	"""docstring for Board"""
	def __init__(self, element):
		youtube = re.findall(YT, element.get_attribute('innerHTML'))
		self.urls = [('Youtube video', url) for url in youtube]
		pedco = element.find_elements_by_tag_name('a')
		self.urls.extend([(a.get_attribute('text'), a.get_attribute('href')) 
			for a in pedco if 'youtu' not in a.get_attribute('href')])
		self.newurls = []

	def diffurl(self, urls):
		self.newurls = [url for url in self.urls if url[1] not in urls]
		return [url[1] + '\n' for url in self.newurls]
