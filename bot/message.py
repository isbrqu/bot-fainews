from datetime import datetime

resource = """
*Materia*: {course}\n
*Descripción*: {description}
*nombre*: {name}\n
_Link: {url}_
"""

def time():
    return datetime.now().strftime('%a %H:%M:%S')
