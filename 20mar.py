'''
Dictionary
-takes the form of key value pairs
used to organise elements into collections
- to access dictionary values, you use keys
- keys in a dictionary must be unique and of immutable data type
- the values can be of any datatype
'''

#creating a dictionary
'''x = {}
print(type(x))
'''
# exmple of a simple dictionary
file_counts = {'jpeg': 10, 'txt': 14, 'csv': 2, 'py': 23}
print(file_counts)

#dict example 2
dictindict = {'info': {'name': 'Ubong Etim', 'age':'22', 'destination': 'Cambridge', 'flightNo': 786534}, 
              'payment': {'mode': 'online transaction', 'amount': 50000.0, 'balance': 0.0 }}

dictindict['info']
print(dictindict['info'])

len(dictindict) #finds the size

# add a new item to dict
dictindict['trip'] = 'one-way'
dictindict['luggage'] = ['bag', 'carry-on']

print(dictindict)


# acess items in a dict
dic_value = file_counts['txt']
print(dic_value)

#dic_val = dictindict['tyl']


#check if the key is contained in thhe dictionary using 'in'
print('jpeg' in file_counts)
print('html' in file_counts)
print('-------------------------------------')


#using a key that doesnot exist will give error
#print(file_counts['tyr'])

#adding a new record to dictionary
print(file_counts)
print('----------------------------')
file_counts['cfg'] = 8
print(file_counts)



#adding a record to a key that already exists, updates that key with a new vale

#print(file_counts)
#print('--------------------')
#file_counts['csv'] = 17
#print(file_counts)

#deletingelements from a dictionary
print('------------------------')
print(file_counts)

del file_counts['cfg']
print(file_counts)


'''
write a program that checks for the key in a dictionary.
if the key is not present, you add it to the dictionary with value   starting from 1
'''

ubong = {'name': 'etim', 'age': 22, 'weight': '70kg'}
print('marriage status' in ubong)
print('----------------------------------')
ubong['marriage status'] = 'single'
print(ubong)



fruits = { 'Apple': 3, 'Bannana': 8, 'Water melon': 3}
moreFruits = ['strwaberry', 'Apple', 'Orange']
for fruit in moreFruits:
    if fruit not in fruits:
        fruits[fruit] = 1
print(fruits)


'''
write a program that creates a dictionary count of all items in a list
'''
colours = ['red', 'blue', 'green', 'yellow', 'green', 'red', 'blue', 'purple', 'orange']
colour_dict ={}
#number = 0
for colour in colours:
    if colour in colour_dict:
        colour_dict[colour] += 1
    else:
        colour_dict[colour] = 1
print(colour_dict)