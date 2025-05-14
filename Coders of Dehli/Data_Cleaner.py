import json
def Data_Cleaner(file_name: str, new_file = None) -> None:
    # Reads a JSON file and writes it back to the same file.

    new_file = file_name if new_file is None else new_file
    # If no new file name is provided, it will overwrite the original file.

    try:
        with open(file_name, 'r') as JSON_File:
            JSON_Data = json.load(JSON_File)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return

    user_data, pages_data = Cleaner(JSON_Data)

    with open(new_file, 'w') as JSON_File:
        json.dump({
            'users': user_data,
            'pages': pages_data
        }, JSON_File, indent=4)

    print('Data Cleaned and written to file successfully............................')


def Cleaner(JSON_Data):
    # Clean the data and return the perfect data
    user_data, pages_data = {}, {}

    # clean the Pages and remove duplicates
    for page in JSON_Data['pages']:
        if int(page['id']) not in pages_data and page['name'].strip():
            pages_data[int(page['id'])] = page['name']

    # clean the Users and remove duplicates also remove inactive users(who donot have friends or liked pages)
    for user in JSON_Data['users']:
        if user['name'].strip() and (user['friends'] or user['liked_pages']):
            # Remove users with missing names or empty friends and liked pages(inactive users).
            user_data[int(user['id'])] = {
                'name': user['name'],
                'friends': list(set(user['friends'])), # Remove duplicate friend entries.
                'liked_pages': list(set(user['liked_pages'])) # Remove duplicate liked pages entries.
            }

    return user_data, pages_data


# Example usage
if __name__ == "__main__":
    Data_Cleaner(file_name= r'massive_data.json', new_file= r'cleaned_data.json')
    # You can replace 'a.json' with the path to your JSON file.
    # The cleaned data will be saved in 'cleaned_data.json' or the same file if no new file name is provided.