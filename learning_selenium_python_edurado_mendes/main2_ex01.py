from selenium.webdriver import Chrome

browser = Chrome()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')

"""
1. Busca o 'ul'
2. Busca todos os 'li'
3. Entro no primeiro 'li' e pego o texto da tag 'a'
"""

not_list_order = browser.find_element_by_tag_name('ul')
lis = browser.find_elements_by_tag_name('li')
text_a = lis[0].find_element_by_tag_name('a').text
url_a = lis[0].find_element_by_tag_name('a').get_attribute('href')

print(text_a)
print("___________________")
print(url_a)

