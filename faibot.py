import re
import telegram
from decouple import config
from datetime import datetime

def escape(text):
	return re.sub(r'([._*`{}\[\]()~>#|!?+=-])', r'\\\1', text)

class Faibot(object):
	"""docstring for Faibot"""
	def __init__(self):
		self.bot = telegram.Bot(token=config('TELEGRAM_BOT_TOKEN'))
		self.my_id = config('TELEGRAM_MY_CHAT')
		self.group_id = config('TELEGRAM_GROUP_CHAT')
		# self.group_id = self.my_id # with test

	def send_nov(self, alias, title, url):
		title = escape(title)
		url = escape(url)
		self.send_group(f'*Materia*: {alias}\n\n*Descripción*: Posteo en Novedades\n{title}\n\n_Link: {url}_')

	def send_photo(self, path):
		self.bot.send_photo(chat_id=self.group_id, photo=open(path, 'rb'))

	def check(self):
		self.send_me(datetime.now().strftime('`%a %H:%M:%S`'))

	def send_me(self, msg, markdown=True):
		if markdown:
			self.bot.send_message(chat_id=self.my_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN_V2)
		else:
			self.bot.send_message(chat_id=self.my_id, text=msg)

	def send_group(self, msg):
		self.bot.send_message(chat_id=self.group_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN_V2)

	def send_url(self, alias, url):
		if 'youtu' in url[1]:
			notice = 'entregado un video de youtube'
		elif 'assign' in url[1]:
			notice = 'asignado una entrega'
		elif 'quiz' in url[1]:
			notice = 'creado un cuestionario'
		elif 'book' in url[1]:
			notice = 'subido libro para ver/realizar'
		elif 'page' in url[1]:
			notice = 'añadido una pagina con contenido a realizar o ver'
		elif 'url' in url[1]:
			notice = 'añadido un enlace como rescurso'
		elif 'resource' in url[1]:
			notice = 'subido un archivo'
		elif 'forum' in url[1]:
			notice = 'habilitado un foro'
		elif 'folder' in url[1]:
			notice = 'añadido una carpeta'
		else:
			notice = None
		name = escape(url[0])
		url = escape(url[1])
		if notice:
			msg = f'*Materia*: {alias}\n\n*Descripción*: Se ha {notice}\n{name}\n\n_Link: {url}_'
			self.send_group(msg)
		else:
			msg = f'*Materia*: {alias}\n\n*Descripción*: Link no categorizado\n{name}\n\n_Link: {url}_'
			self.send_me(msg)

	def _send(self, chat_id, msg):
		self.bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN_V2)
