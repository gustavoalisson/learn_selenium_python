from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# * BROWNSER
brownser = webdriver.Chrome()
brownser.get('https://demoqa.com/upload-download')
brownser.maximize_window()

# * SELECTORS
input_file_upload = '//*[@id="uploadFile"]'

# * ELEMENTS
brownser.find_element_by_xpath(input_file_upload).send_keys(
    r'C:\Users\Alisson Gustavo\Downloads\sampleFile.jpeg')
