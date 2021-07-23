from selenium.webdriver import Chrome
from time import sleep
from pprint import pprint

browser = Chrome()

browser.get('http://selenium.dunossauro.live/aula_04.html')

def get_links(browser, element):
    # pega todos os links dentro de um elemento
    resultado = {}
    find_element = browser.find_element_by_id(element)
    ancoras = find_element.find_elements_by_tag_name('a')
    
    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')
    
    return resultado
sleep(2)

exercicio = get_links(browser, 'aside')

pprint(exercicio)

browser.get(exercicio['Aula 3'])    

