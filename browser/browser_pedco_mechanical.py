from datetime import datetime
from .mechanical_moodle import MechanicalMoodle

database = PedcoDatabase()

class PedcoBrowser(MechanicalMoodle):

    def __init__(self):
        super().__init__()

    @property
    def period(self):
        return (1 if datetime.now().month < 6 else 2)

    def update_resources(self):
        for course in database.current_curses:
            self.open_with_session(course.url)
            print(f'course: {course.name}')
            for a in self.page.select('#region-main a[href]'):
                database.save_resource(course, a)

    def update_discussions(self):
        for forum in database.current_forums:
            self.open_with_session(forum.url)
            print(f'forum: {forum.name}')
            for tr in self.page.select('tr.discussion'):
                database.save_discussion(forum, tr)

