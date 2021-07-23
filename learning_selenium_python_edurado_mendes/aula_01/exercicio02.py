from time import sleep
from selenium.webdriver import Chrome

browser = Chrome()
browser.get('https://curso-python-selenium.netlify.app/exercicio_02.html#')

sleep(3)

tag_p = browser.find_elements_by_tag_name('p')
tag_a = browser.find_element_by_tag_name('a')

sleep(2)

    # text_p = tag_p[-1].text
    # print(text_p)
    # sleep(1)
    # tag_a.click()
    
for click in browser.find_elements_by_tag_name('p'):
    sleep(1)
    tag_a.click()

    
