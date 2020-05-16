from selenium.common.exceptions import NoSuchElementException

class BasePage():
	# Это конструктор (объявляется ключевым словом __init__). Конструктор — метод, который вызывается, когда мы создаем объект
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	# Метод open должен открывать нужную страницу в браузере, используя метод get()
	def open(self):
		self.browser.get(self.url)

	# Чтобы перехватывать исключение
	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			return False
		return True