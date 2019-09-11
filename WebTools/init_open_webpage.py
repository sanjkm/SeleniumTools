from selenium import webdriver
import time

chrome_driver_location = '/usr/bin/chromedriver'

def initOpenWebPage (url_name):

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument("--test-type")

    driver = webdriver.Chrome(chrome_driver_location, chrome_options=options)
    driver.get(url_name)

    return driver


