from datetime import datetime
from models import Course, Forum
from .mechanical_moodle import MechanicalMoodle

class PedcoBrowser(MechanicalMoodle):

    def __init__(self):
        super().__init__()
        self.courses1 = Course.everyone_in_the_period(1)
        self.courses2 = Course.everyone_in_the_period(2)

    @property
    def period(self):
        return (1 if datetime.now().month < 6 else 2)

    @property
    def courses(self):
        return (self.courses1 if self.period == 1 else self.courses2)

    @property
    def forums(self):
        return Forum.everyone_in_the_period(self.period)

    def update_resources(self):
        for course in self.courses:
            self.open_with_session(course.url)
            print(f'course: {course.name}')
            for a in self.page.select('#region-main a[href]'):
                writer.resource(course, a)

    def update_discussions(self):
        for forum in self.forums:
            self.open_with_session(forum.url)
            print(f'forum: {forum.name}')
            for tr in self.page.select('tr.discussion'):
                writer.discussion(forum, tr)

