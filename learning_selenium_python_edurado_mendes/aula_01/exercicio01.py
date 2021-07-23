from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep

browser = webdriver.Chrome()
browser.get('https://curso-python-selenium.netlify.app/exercicio_01.html')

sleep(3)

h1 = browser.find_element_by_tag_name('h1')
text_h1 = h1.text

texto1 = browser.find_element_by_xpath('/html/body/p[1]')
texto2 = browser.find_element_by_xpath('/html/body/p[2]')
texto3 = browser.find_element_by_xpath('/html/body/p[3]')

atributo1 = texto1.get_attribute('atributo')
atributo2 = texto2.get_attribute('atributo')
atributo3 = texto3.get_attribute('atributo')


dicionary = text_h1 , f'= {{ {atributo1}: {texto1.text} , {atributo2}: {texto2.text} , {atributo3}: {texto3.text}  }}'

print(dicionary)
 