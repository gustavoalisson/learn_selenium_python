from selenium.webdriver import Chrome
from urllib.parse import urlparse

browser = Chrome()

browser.get('http://selenium.dunossauro.live/aula_04_b.html')

url_status = urlparse(browser.current_url)

print('AQUI >>>>', browser.title)
print(url_status)