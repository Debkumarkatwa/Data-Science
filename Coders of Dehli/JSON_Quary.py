# The code is a simple JSON query program that allows users to retrieve information about users and pages from a JSON file.
import json
import Data_Cleaner as DC
import os

def Clean_load_json(filename):
    DC.Data_Cleaner(filename, new_file = 'cleaned_data.json') # This function cleans the JSON data and saves it to a new file
    
    with open('cleaned_data.json', 'r') as file:
        data = json.load(file)
    return data

# This function retrieves user data based on the user ID.
def get_user_data(user_id):
    user = Users.get(user_id)
    
    if user:
        return f'''
            User ID: {user_id} --> 
                '{user['name']}' is friends of {[Users[str(friend)]['name'] for friend in user['friends'] if str(friend) in Users]} and 
                likes the pages {[data['pages'][str(page)] for page in user['liked_pages']]}.
            '''
    else:
        return '\tNo Data Found for This User\n'


# Load the JSON data from the file
data = Clean_load_json('a.json') # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
global Users
Users = data['users']

# ------------------------------------------------------------------------------
print('Welcome to the JSON Query Program\n')
option = 1
while option:
    print('Select "0" for EXIT:-------------------')
    option = input('Enter the user ID: ')
    match option:
        case '0':
            print('\nExiting the program...')
            os.remove('cleaned_data.json')  # Clean up the temporary file
            break
        case _:
            print(get_user_data(option))