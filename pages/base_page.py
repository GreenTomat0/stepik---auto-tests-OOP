class BasePage():
	# Это конструктор (объявляется ключевым словом __init__). Конструктор — метод, который вызывается, когда мы создаем объект
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url

	# Метод open должен открывать нужную страницу в браузере, используя метод get()
	def open(self):
		self.browser.get(self.url)