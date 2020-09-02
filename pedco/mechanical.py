from mechanicalsoup import StatefulBrowser
from message import TITLE_LOGIN
from decouple import config

URL_BASE = 'https://pedco.uncoma.edu.ar/'
URL_LOGIN = URL_BASE + 'login/index.php'
URL_HOME = URL_BASE + 'my/'
URL_COURSE = URL_BASE + 'course/view.php?id=%d'
URL_FORUM = URL_BASE + 'mod/forum/view.php?id=%d'
TITLE_LOGIN = 'PEDCO: Entrar al sitio'

class Mechanical(StatefulBrowser):
    """docstring for Mechanical"""
    def __init__(self, subjects=[]):
        super().__init__()
        self.courses = Course.all()
        self.mod = Collection([])
        self.mod_data = []
        self.mod_bigbluebuttonbn = []
        self.mod_chat = []
        self.mod_choice = []
        self.mod_quiz = []
        self.mod_journal = []
        self.mod_feedback = []
        self.mod_survey = []
        self.mod_forum = []
        self.mod_glossary = []
        self.mod_lti = []
        self.mod_hotpot = []
        self.mod_jitsi = []
        self.mod_lesson = []
        self.mod_scorm = []
        self.mod_workshop = []
        self.mod_assign = []
        self.mod_wiki = []
        self.mod_resource = []
        self.mod_folder = []
        self.mod_label = []
        self.mod_book = []
        self.mod_page = []
        self.mod_imscp = []
        self.mod_url = []
        self.mod_youtube = []
        self.mod_meet = []
        self.mod_unknow = []
        self._extract_mod()

    @property
    def page(self):
        return super().get_current_page()

    @property
    def url(self):
        return self.get_url()

    @property
    def title(self):
        return self.page.title.text

    @property
    def in_login(self):
        return (self.url == URL_LOGIN)

    @property
    def logged_in(self):
        return not self.in_login

    def open(self, url):
        success = False
        while not success:
            try:
                super().open(url, timeout=5)
                success = True
            except Exception as e:
                print(e)
                time.sleep(2)
        return success

    def open_with_session(self, url):
        success = False
        while not success:
            if self.in_login:
                print('se ha cerrado la sesión')
                self.loginenv()
            else:
                success = True
                self.open(url)
        return success

    def login(self, username, password):
        self.open(urlp.LOGIN)
        if self.page.find('h4'):
            self.select_form(nr=1)
        else:
            self.select_form()
            self['username'] = username
            self['password'] = password
        self.submit_selected()
        success = self.logged_in
        if success and not self.courses:
            self._update_courses()
        return success

    def _update_courses(self):
        nav = self.page.select_one('#nav-drawer')
        links = nav.find_all('a', {'data-parent-key': 'mycourses'})
        self.subjects = []
        for a in links:
            self.subjects.append({
                'name': a.text.replace('\n', '').lower(),
                'url': a['href']
            })

    def _extract_mod(self):
        for a in element.find_elements_by_tag_name('a'):
            name = a.get_attribute('text')
            url = a.get_attribute('href')
            mod = {'name': name, 'url': url}
            self.mod.append(mod)
            if 'data' in url:
                self.mod_data.append(mod)
            elif 'bigbluebuttonbn' in url:
                self.mod_bigbluebuttonbn.append(mod)
            elif 'chat' in url:
                self.mod_chat.append(mod)
            elif 'choice' in url:
                self.mod_choice.append(mod)
            elif 'quiz' in url:
                self.mod_quiz.append(mod)
            elif 'journal' in url:
                self.mod_journal.append(mod)
            elif 'feedback' in url:
                self.mod_feedback.append(mod)
            elif 'survey' in url:
                self.mod_survey.append(mod)
            elif 'forum' in url:
                self.mod_forum.append(mod)
            elif 'glossary' in url:
                self.mod_glossary.append(mod)
            elif 'lti' in url:
                self.mod_lti.append(mod)
            elif 'hotpot' in url:
                self.mod_hotpot.append(mod)
            elif 'jitsi' in url:
                self.mod_jitsi.append(mod)
            elif 'lesson' in url:
                self.mod_lesson.append(mod)
            elif 'scorm' in url:
                self.mod_scorm.append(mod)
            elif 'workshop' in url:
                self.mod_workshop.append(mod)
            elif 'assign' in url:
                self.mod_assign.append(mod)
            elif 'wiki' in url:
                self.mod_wiki.append(mod)
            elif 'resource' in url:
                self.mod_resource.append(mod)
            elif 'folder' in url:
                self.mod_folder.append(mod)
            elif 'label' in url:
                self.mod_label.append(mod)
            elif 'book' in url:
                self.mod_book.append(mod)
            elif 'page' in url:
                self.mod_page.append(mod)
            elif 'imscp' in url:
                self.mod_imscp.append(mod)
            elif 'url' in url:
                self.mod_url.append(mod)
            elif 'youtube.com' in url or 'youtu.be' in url:
                self.mod_youtube.append(mod)
            elif 'meet.google.com' in url:
                self.mod_meet.append(mod)
            else:
                self.mod_unknow.append(mod
