import json
def People_You_Might_Know(data: dict, userid):
    priority = {}
    a = []
    for i in data[userid]:  # loop through the direct friends of the user
        a.extend(data[i])   # get the mutual friends (1 id may occour multiple times that become the priority)
        
    for i in a:         # loop through the mutual friends
        if i != userid and i not in data[userid]:
            priority[i] = priority.get(i, 0) + 1    # update the priority count

    return [x[0] for x in sorted(priority.items(), key=lambda x: x[1], reverse=True)]


# ----------- Main Function ---------
with open('massive_data.json', 'r') as f:
        users = json.load(f)['users']
    
My_JSON_Data = {
    user['id']: user['friends'] for user in users
}
result = People_You_Might_Know(
    My_JSON_Data,
    userid= int(input("Enter User ID: "))
)
print(f'user might know people with ids {result}') 



'''             # Harry's Approach
import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

def find_people_you_may_know(user_id, data):
    user_friends = {}
    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])
    
    if user_id not in user_friends:
        return []
    
    direct_friends = user_friends[user_id]
    suggestions = {}
    
    for friend in direct_friends:
        # For all friends of friend
        for mutual in user_friends[friend]:
            # If mutual id is not the same user and not already a direct friend of user
            if mutual != user_id and mutual not in direct_friends:
                # Count mutual friends
                suggestions[mutual] = suggestions.get(mutual, 0) + 1
    
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [user_id for user_id, _ in sorted_suggestions]

# Load data
data = load_data("cleaned_codebook_data.json")
user_id = 1  # Example: Finding suggestions for Amit
recommendations = find_people_you_may_know(user_id, data)
print(f"People You May Know for User {user_id}: {recommendations}")
'''
