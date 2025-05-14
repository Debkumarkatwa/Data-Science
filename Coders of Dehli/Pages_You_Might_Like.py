import json
def Pages_You_Might_Like(data: dict, userid):
    pages = {}

    for user in data.keys():
        if user != userid:
            a, b = set(data[user]), set(data[userid])
            value = set(a - b)  # get the pages that user liked but not the Searched user
            key = len( list(a.intersection(b)) )  # get the number of common pages liked by both users(priority) 

            if key in pages.keys():
                pages[key].update(value)
            else:
                pages[key] = value
                
    pages = dict(sorted(pages.items(), key=lambda item: item[0], reverse=True))
    
    result = []
    for i in pages.keys():
        result.extend(list(set(pages[i] - set(result))))  # adding the pages to the result list(removing duplicates using set difference)
        
    return result


# --------- Main Function ---------
with open('massive_data.json', 'r') as f:
        users = json.load(f)['users']
    
My_JSON_Data = {
    user['id']: user['liked_pages'] for user in users
}

result_2 = Pages_You_Might_Like(
    data= My_JSON_Data,
    userid= 2
)
print(result_2)




'''                 # Harry's Approch
import json

# Function to load JSON data from a file
def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Function to find pages a user might like based on common interests
def find_pages_you_might_like(user_id, data):
    # Dictionary to store user interactions with pages
    user_pages = {}
    for user in data["users"]:
        user_pages[user["id"]] = set(user["liked_pages"])
    
    # If the user is not found, return an empty list
    if user_id not in user_pages:
        return []
    
    user_liked_pages = user_pages[user_id]
    page_suggestions = {}
    
    for other_user, pages in user_pages.items():
        if other_user != user_id:
            shared_pages = user_liked_pages.intersection(pages)
            for page in pages:
                if page not in user_liked_pages:
                    page_suggestions[page] = page_suggestions.get(page, 0) + len(shared_pages)
    
    # Sort recommended pages based on the number of shared interactions
    sorted_pages = sorted(page_suggestions.items(), key=lambda x: x[1], reverse=True)
    return [page_id for page_id, _ in sorted_pages]

# Load data
data = load_data("cleaned_codebook_data.json")
user_id = 1  # Example: Finding recommendations for Amit
page_recommendations = find_pages_you_might_like(user_id, data)
print(f"Pages You Might Like for User {user_id}: {page_recommendations}")
'''