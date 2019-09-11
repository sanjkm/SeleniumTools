# TestSelenium.py

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
driver.get('https://python.org')
