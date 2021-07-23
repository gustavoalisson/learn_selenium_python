from selenium.webdriver import Chrome
from time import sleep

# DOM = Document Object Model 
# Arquitetura do DOM, Tags dentro tags (Estrutura de árvore)
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Chrome()
browser.get(url)

sleep(2)

tag_a = browser.find_element_by_tag_name('a')

for i in range(20):
    tag_p = browser.find_elements_by_tag_name('p')
    tag_a.click()
    print(f'Valor do ultimo p: {tag_p[-1].text} valor do click: {i}')
    
    print(f'Os valores são iguais {tag_p[-1].text == str(i)}')