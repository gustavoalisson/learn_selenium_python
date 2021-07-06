from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert

# * BROWNSER
brownser = webdriver.Chrome()
brownser.get('https://demoqa.com/alerts')
brownser.maximize_window()

# * ALERT
alert = Alert(brownser)

# * SELECTORS
btn_alert = '//*[@id="alertButton"]'

# * FIND ELEMENTS
findBtnAlert = brownser.find_element_by_xpath(btn_alert)

# * FUNCTION TO CLICK IN FIRT ALERT
findBtnAlert.click()

sleep(2)
# ! Exemplo usando da função Alert do Selenium
alert.accept()
