# dateTimePick.py
# Functions that automate selecting a time and calendar date
# where they must be clicked within their choices
# send_keys will not work for these

from selenium.webdriver.support.ui import Select
import time
from datetime import datetime

def convertTimeInttoStr (time_int):

    if time_int > 2359 or time_int < 0:
        print 'Invalid time_int %s' % str(time_int)
        exit()

    hour_num = time_int / 100
    minute_num = time_int % 100

    if minute_num >= 60:
        print 'Invalid time_int %d' % time_int
        exit()

    if hour_num == 0:
        hour_num = 12
        time_of_day = 'AM'
    elif hour_num < 12:
        time_of_day = 'PM'
    else:
        if hour_num != 12:
            hour_num = hour_num - 12
        time_of_day = 'PM'

    hour_str, minute_str = str(hour_num), str(minute_num)
    
    if minute_num < 10:
        minute_str = '0' + minute_str
        
    time_str = hour_str + ':' + minute_str + ' ' + time_of_day

    return time_str
        

# find_dict is the key by which we find the time choice box to click
# Assumes time is in a drop down box
# May not work in a different setup
def timePickDropdown (driver, find_dict, time_int):

    if 'id' in find_dict:
        id_name = find_dict['id']
        
        mySelect = Select(driver.find_element_by_id (id_name))

    else:
        print 'No functionality to handle this case yet'
        exit()

    time_list = [o.text for o in mySelect.options]

    time_str = convertTimeInttoStr (time_int)

    time_str_index = time_list.index (time_str)

    mySelect.select_by_index(time_str_index)

    return driver

# Takes display date in the calendar box as inputs,
# returns number of months must click to arrive at month for
# date_str
def calcDisplayMonthDiff (disp_mo, disp_yr, meeting_date):

    months_in_yr = 12

    num_years = meeting_date.year - disp_yr

    num_mos = meeting_date.month - disp_mo

    total_mos = (months_in_yr * num_years) + num_mos

    return total_mos

    
    
    

def datePick (driver, find_dict, date_str,
              date_str_format = '%Y-%m-%d'):

    if 'name' in find_dict:
        label_name = find_dict['name']
        
        driver.find_element_by_name (label_name).click()

    else:
        print 'No functionality to handle this case yet'
        exit()

    time.sleep(5)

    displayed_month_yr = driver.find_element_by_xpath ("//div[@role='heading']").text.split(' ')

    mo_name_str, yr = displayed_month_yr[0], int(displayed_month_yr[1])

    mo_num = datetime.strptime (mo_name_str, '%B').month

    meeting_date = datetime.strptime (date_str, date_str_format)

    num_month_clicks = calcDisplayMonthDiff (mo_num, yr, meeting_date)

    for i in range(num_month_clicks):

        time.sleep(5)

        element = driver.find_element_by_xpath("//*[local-name()='svg'][@class='svg svg--chevron-right svg-icon valign--middle']")

        element.click()

    time.sleep(2)
        
    driver.find_element_by_xpath("//*[local-name()='time'][@datetime='" + date_str + "']").click()

    time.sleep(5)

    return driver

