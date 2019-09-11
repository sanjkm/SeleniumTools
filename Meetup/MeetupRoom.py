# MeetupRoom.py
# Login to meetup, book a WeWork room

import os, sys
import time

from NavigateMeetup import *

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(dir_path)

sys.path.append(parent_dir + '/WebTools')
from init_open_webpage import initOpenWebPage
from login_webpage import loginWebPage
from inputs import *

if __name__ == '__main__':

    gen_input_dict, user_dict = getGeneralInputs(), getUserInputs()

    driver = initOpenWebPage (gen_input_dict['url'])

    driver = loginWebPage (driver, gen_input_dict['username'],
                           gen_input_dict['password'],
                           submit_type = gen_input_dict['submit_type'])

    driver = checkAvailabilityPage (driver)

    driver = gotoSchedulePage (driver)

    driver = pickDateTime (driver, user_dict['date'],
                           user_dict['start_time'],
                           user_dict['end_time'])

    pickRoom (driver)

    
    
