'''
looping over a dictionary
'''
#iterating over a dictionary and uing the keys to get corresponding values
file_counts = {'jpg':10, 'txt':14, 'csv':2, 'py':23}
for file in file_counts:
    print(file) #prints the keys
print('-------------------------------------------------------------------------------')
for file in file_counts:
    print(file_counts[file])# prints the values

print('-----------------------------------------------------------------------------------')
#functions used with a dictionary
# dictionary.keys() prints the keys
for key in file_counts.keys():
    print(key)
print('--------------------------------------------------------------------------------')
# dicitonary.values() prints the values
for value in file_counts.values():
    print(value)
print('-------------------------------------------------------------------------------')
# dictionary.items() rpints both keys and values
for item in file_counts.items():
    print(item)
     
#example is a function for counting how many times each letter occurs in a piece of text
#the result is a dictioanry where the keys are each letter in the present string
#and the values are howmany times each letter is present
String= input('input a string: ')
 


def countLetters(String):
    letterDict = {}
   # String.replace(' ', '')
    for letter in String:
        if letter != ' ' and  letter not in letterDict:
             
            letterDict[letter] = 1
        elif  letter != ' ':
            letterDict[letter] +=1

    return letterDict  

ans = countLetters(String)

print(ans)

