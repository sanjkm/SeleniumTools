# inputs.py
# All general specific inputs to the program should reside here

# These should be updated each time the program is run
def getUserInputs ():

    input_dict = {}

    input_dict['date'] = '2019-12-03'
    input_dict['start_time'] = 1800
    input_dict['end_time'] = 2000

    return input_dict

# These should generally stay the same, unless Meetup changes things on
# their end
def getGeneralInputs ():

    input_dict = {}
    
    url_name = 'https://www.meetup.com/newyorkcity-ptsd/explore-spaces/schedule'

    input_dict['url'] = url_name 
    input_dict['username'] = 'sanjay'
    input_dict['password'] = 'XXX'
    input_dict['submit_type'] = 'submitButton'

    return input_dict
