from PIL import Image
from io import BytesIO
from datetime import datetime
from .selenium_moodle import SeleniumMoodle

FOLDER = 'img'

class SeleniumPedco(SeleniumMoodle):

    def __init__(self):
        super().__init__()

    def screenshot(self, url, name):
        self.open_with_session(url)
        dimensions = self._calculate_dimensions_discussion()
        path = self._generate_path(name)
        Image.open(BytesIO(self.get_screenshot_as_png()))\
            .crop(dimensions)\
            .save(path)
        return path

    def _generate_path(self, name):
        date = datetime.now().strftime('%m-%d-%H-%M-%S')
        return f'{FOLDER}/{name}-{date}.png' 

    def _calculate_dimensions_discussion(self):
        tag = self.find_element_by_tag_name('article')
        return self._calculate_dimensions(tag)

    def _calculate_dimensions(self, tag):
        location, size = tag.location, tag.size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        return (left, top, right, bottom)

