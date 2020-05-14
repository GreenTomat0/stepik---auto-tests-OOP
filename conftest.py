import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
	parser.addoption('--language', action='store', default=None,
					help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
	user_language = request.config.getoption("language")#'en,en_US'#
	print("\nstart browser for test..")

	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
	browser = webdriver.Chrome(options=options)
	
	'''
	fp = webdriver.FirefoxProfile()
	fp.set_preference("intl.accept_languages", user_language)
	browser = webdriver.Firefox(firefox_profile=fp)
	'''

	yield browser
	print("\nquit browser..")
	browser.quit()