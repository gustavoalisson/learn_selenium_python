from selenium import webdriver
from time import sleep


# * BROWNSER
brownser = webdriver.Chrome()
brownser.get('https://demoqa.com/alerts')
brownser.maximize_window()

# * SELECTORS
btn_alert = '//*[@id="alertButton"]'
btn_box_insert_text = '//*[@id="promtButton"]'

# * FIND ELEMENTS
findBtnAlert = brownser.find_element_by_xpath(btn_alert)
findBtnPrompt = brownser.find_element_by_xpath(btn_box_insert_text)

# * FUNCTION TO CLICK IN FIRT ALERT
findBtnAlert.click()

# * SWITCH TO
alert = brownser.switch_to.alert

print(alert.text)
sleep(2)
alert.accept()

sleep(2)

# ! Refazendo o processo, mas clicando em um alert que necessita digitar um texto

# * FUNCTION TO CLICK ON LAST ALERT
findBtnPrompt.click()

# * SWITCH TO REPEAT
alert_two = brownser.switch_to.alert
alert.send_keys('Testando a função de interagir com ALERTS!!! HEHE')
sleep(2)
alert.accept()
