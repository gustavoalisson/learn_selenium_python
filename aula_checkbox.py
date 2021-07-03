from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice

list_of_selector_1 = ['#tree-node > ol > li > ol > li:nth-child(1) > span > button > svg',
                      '#tree-node > ol > li > ol > li:nth-child(2) > span > button > svg',
                      '#tree-node > ol > li > ol > li:nth-child(3) > span > button > svg']

arrow_down = [
    'tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > span > button > svg']


list_desktop_selector = ['#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-title',
                         '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span > label > span.rct-title']

list_documents_selector = ['#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > button > svg',
                           '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span > button > svg']

list_downloads_selector = ['#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label',
                           '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span > label']

# * NAVEGADOR
brownser = webdriver.Chrome()
brownser.get('https://demoqa.com/checkbox')
brownser.maximize_window()

# * SELETORES
buttonView = '#tree-node > ol > li > span > button'  # SELECTOR

selectOptions = choice(list_of_selector_1)

selectOptionsDesktop = choice(list_desktop_selector)
selectOptionsDocuments = choice(list_documents_selector)
selectOptionsDownloads = choice(list_downloads_selector)

# * ELEMENTOS
brownser.find_element_by_css_selector(buttonView).click()
sleep(1)
brownser.find_element_by_css_selector(selectOptions).click()
sleep(2)


if(arrow_down):
    brownser.find_element_by_css_selector(selectOptionsDesktop).click()

elif(arrow_down):
    sleep(2)
    brownser.find_element_by_css_selector(selectOptionsDocuments).click()

elif(arrow_down):
    sleep(2)
    brownser.find_element_by_css_selector(selectOptionsDownloads).click()
