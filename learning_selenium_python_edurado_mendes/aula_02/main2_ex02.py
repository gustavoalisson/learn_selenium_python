from selenium import webdriver
from selenium.webdriver import Chrome

def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag)
    
    for elemento in elementos:
        if elemento.text == text:
            return elemento
        
browser = webdriver.Chrome()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

element_ddg = find_by_text(browser, 'li', 'DuckDuckGo')

print(element_ddg.text)

