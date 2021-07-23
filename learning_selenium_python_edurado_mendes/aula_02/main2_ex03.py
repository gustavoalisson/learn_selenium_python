from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep

def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag)
    
    for elemento in elementos:
        if elemento.text == text:
            return elemento

def back(browser):
    for i in range(4):
        sleep(1)
        browser.back()
        
def go(browser):
    for i in range(4):
        sleep(1)
        browser.forward()            

browser = webdriver.Chrome()

browser.get('http://selenium.dunossauro.live/aula_04_b.html')

name_box = ['um', 'dois', 'tres', 'quatro']

for text in name_box:
    sleep(1)
    find_by_text(browser, 'div', text).click()

back(browser)
go(browser)

        