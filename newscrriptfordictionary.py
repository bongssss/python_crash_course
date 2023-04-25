"""Create a function groups_per_user, The function receives a dictionary,
 which contains group names with the list of users. Users can belong to 
 multiple groups. The function will return a dictionary with the users as keys
  and a list of their groups as values."""
#Example of data you can use to run the function:
user_groups = {"local": ["admin", "userA"],
		       "public":  ["admin", "userB"],
		       "administrator": ["admin"] }


print('Initial Group of users ', user_groups)

'-------------------------------------------------------------------'

"""
class example
Write a function will add "admin' and 'userB'  to a new group called 'owner'
"""


def add_group(dict, Update_list):
    """Updates the dict with each item of the list

    var: dict, list
    return: dictionary
    
    """
    for new_item in Update_list:
        dict.update(new_item) 
    return dict

add_group(user_groups, [{"dev":['admin','UserA']}, {"Owner":["admin", "UserB"]}])

print("The updated list is ", user_groups ) 


def groups_per_user(dictionary):
    """
    This function takes a dictionary containing group names with a list as users

    arg: Dicitonary

    return: group_dict

    """
    groups_dict = {}
    for group, users in dictionary.items():
        for user in users:
            if user not in groups_dict:
                groups_dict[user] = [group]
            if group not in groups_dict[user]:
                groups_dict[user].append(group)
    return groups_dict

print("list of users and the new groups they belong to:")
print(groups_per_user(user_groups))




#assignment
"""
Grocery will be dictionary of an item with a unit price. Your function is going to be
add price 
""" 
"""
create add_prizes function that returns the total price of all of te groceries
in the dictionary

groceries = {item: unit_price}
 def add_price(basket)

 add_prizes(groceries)
"""

