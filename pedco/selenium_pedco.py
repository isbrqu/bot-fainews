from PIL import Image
from io import BytesIO
from datetime import datetime
from .selenium_moodle import SeleniumMoodle

class SeleniumPedco(SeleniumMoodle):

    def __init__(self):
        super().__init__()

    def screenshot_article(self, forum):
        self.open_with_session(forum.url)
        dt = datetime.now().strftime('%m-%d-%H-%M-%S')
        path = f'img/{name}-{dt}.png'
        Image.open(
            BytesIO(self.get_screenshot_as_png())
        ).crop(
            self._calculate_dimensions(
                self.find_element_by_tag_name('article')
            )
        ).save(path)
        return path

    def _calculate_dimensions(self, tag):
        location, size = tag.location, tag.size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        return (left, top, right, bottom)

