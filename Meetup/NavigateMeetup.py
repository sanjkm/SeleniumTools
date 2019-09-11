import selenium
import os, time, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(dir_path)

sys.path.append(parent_dir + '/WebTools')
from dateTimePick import timePickDropdown, datePick

def checkAvailabilityPage (driver):

    xpath = '//button[normalize-space()="Check availability"]'

    driver.find_element_by_xpath(xpath).click()

    # time.sleep(5)

    return driver

def gotoSchedulePage (driver):
    
    continue_button_id = 'irlContinueBtn'

    driver.find_element_by_id(continue_button_id).click()

    time.sleep(5)
    
    return driver

def pickDateTime (driver, date_str, start_time, end_time):

    find_dict = {}
    start_time_id, end_time_id = 'irlStartTimeSelect', 'irlEndTimeSelect'
    date_label_name = 'selectedDate'
    
    find_dict['id'] = start_time_id

    driver = timePickDropdown (driver, find_dict, start_time)
    
    find_dict['id'] = end_time_id

    driver = timePickDropdown (driver, find_dict, end_time)

    find_dict['name'] = date_label_name

    driver = datePick (driver, find_dict, date_str)

    return driver

def pickRoom (driver):

    room_id = 'irlSelectRoom-5591'

    driver.find_element_by_id (room_id).click()  # clicks on the room

    time.sleep(5)

    # click checkbox agreeing to terms
    checkbox_xpath = "//span[@role='checkbox']"
    
    element = driver.find_element_by_xpath(checkbox_xpath)
    element.click()

    reserve_button_id = 'irlReserveSpaceBtn'

    driver.find_element_by_id (reserve_button_id).click() # reserves room

    time.sleep(5)

    # don't schedule meetup just now
    not_now_schedule_id = "irlNotNowReservationSuccessLink" 

    driver.find_element_by_id (not_now_schedule_id).click()

    return 0

    
