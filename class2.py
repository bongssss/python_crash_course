'''
class 2
write a programme that will take a persons name and return a greeting

solution

progeam should ask for a name,
save the name to a variable
return a greeting


classwork 
 the groups_per_user function receives a dictionary, that contains group names with the list of users.
 Users can belong in multiple groups.
 the function will return a dictionary with the users as keys and the list of their groups as values 
  
'''''
#write a program that will add admin and userB to a new group called 'owner'
#solution 
group_users = {'Local': ['admin', 'userA'],
               'public':['admin', 'userB'],
               'administrator': ['admin'],
               'dev':['admin', 'userA']}
print('initial group and users', group_users)

def add_group(dict, update_list): #pdates the dict with each item on the list
    # var: dict, list
    #return dict
      for new_item in update_list:
        dict.update(new_item)
      return dict




def add_group (dict, list): #updates the dictionary with each item of the list
    # var: dict, list
    #return dict
    for new_item in list:
        dict.update(new_item)
    return dict

add_group(group_users, [])    

#write a program that will add admin and userB to a new group called 'owner





