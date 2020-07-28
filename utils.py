import re

URL_BASE = 'https://pedco.uncoma.edu.ar/'
URL_LOGIN = URL_BASE + 'login/index.php'
URL_MY = URL_BASE + 'my/'
URL_COURSE = URL_BASE + 'course/view.php?id=%d'
URL_FORUM = URL_BASE + 'mod/forum/view.php?id=%d'

# espaca caracteres especiales de markdown de telegram
def escape(text):
    return re.sub(r'([._*`{}\[\]()~>#|!?+=-])', r'\\\1', text)
