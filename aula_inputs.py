from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# * NAVEGADOR
brownser = webdriver.Chrome()
brownser.get('https://demoqa.com/text-box')
brownser.maximize_window()

# * SELETORES
input_name = '//*[@id="userName"]'
input_email = 'userEmail'
input_address = 'currentAddress'

# * ELEMENTOS
inputNameElement = brownser.find_element_by_xpath(input_name)
inputEmailElement = brownser.find_element_by_id(input_email)
inputAddressElement = brownser.find_element_by_id(input_address)

# * FUNCÃO PARA CLIQUE
inputNameElement.click()
inputEmailElement.click()
inputAddressElement.click()

# * DIGITAR VALORES
inputNameElement.send_keys('Alisson Gustavo')
inputEmailElement.send_keys('email@gmail.com')
inputAddressElement.send_keys('Primeira Rua do Colégio')
