# login_webpage.py
# fill in username, password, and log in given a driver and various
# information to the page

from selenium import webdriver

def loginWebPage (driver, user_login, user_password,
                  email_id='email', password_id='password',
                  submit_type='submit'):
    
    username = driver.find_element_by_id(email_id)
    password = driver.find_element_by_id(password_id)

    username.send_keys(user_login)
    password.send_keys(user_password)

    driver.find_element_by_name(submit_type).click()

    return driver
