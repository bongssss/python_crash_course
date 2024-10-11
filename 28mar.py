'''
THE ANONYMOUS FUNCTION:
ALSO CALLED THE LAMBDA FUNCTION a quicker way of writing functions on the fly 
   when you dont want to save the function itself
'''
#lambda function
raise_to_power = lambda x, y: x ** y 
print(raise_to_power(8,2))
print('-----------------------------------------------------------------')
#to actual function
def toPower(c,d):
    return c ** d
#to longer version of actual function
def raiseToPower(a,b):
    square = a ** b
    return square
ans = toPower(5, 2)
print(ans)


#convert to lambda function
def echo_word(word, echo):
    '''write an expression that will repeat word echo number of times''' 
    return word ** echo
# converting to lambda
echoWord = lambda wordd, echoo: wordd ** echoo 
print('------------------------------------------------------------------')

#FOR LOOP THAT APPENDS ITEMS ON A LIST TO ANOTHER LIST BUT MAKES THEM UPPERCASE
color = ['red', 'blue', 'green']
upper_color = []
for item in color:
   upper_color.append(item.upper())
print(upper_color)
print('--------------------------------------------------------------------')

# write using list comprehension
newColor = [item.upper() for item in color]
print(newColor)
print('--------------------------------------------------------------------')

#USING FOR LOOP IN  A LAMBDA FUNCTION WITH A LIST COMPREHENSION
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myListComp = [(lambda x: x * x)(x) for x in myList]
print('--------------created using list comprehension and lambda---------------')
print(myListComp)
'''
MAP funtion
map function is a built in function that allows you to process and transform items in an iterable
without using an explicit for loop. 
It is useful when you need to apply a transformation function
to each item in an iterable to transform them into a new iterable 
'''

def square(num):
    return num ** 2
ages = [8, 5, 12, 9, 16]
print(list(map(square, ages)))
print('-----------------------------------------------------')


age =[8, 5, 12, 9, 16]
print(list(map(lambda num: num ** 2, age)))







'''
The permissions of a file in a Linux system are split into three sets of

three permissions: read, write, and execute for the owner, group, and

others. Each of the three values can be expressed as an octal number

summing each permission, with 4 corresponding to read, 2 to write, and 1

to execute. Or it can be written with a string using the letters r, w, and

x or - when the permission is not granted. For example: 640 is read/write

for the owner, read for the group, and no permissions for the others;

converted to a string, it would be: "rw-r-----" 755 is read/write/execute

for the owner, and read/execute for group and others; converted to a

string, it would be: "rwxr-xr-x" Write a function that will

convert a permission in octal format into a string format.

# For Example

print (octal_to_string(755)) # Should be rwxr-xr-x

print(octal_to_string(644)) # Should be rw-p--p--

print(octal_to_string(750)) # Should be rwxr-x---

print(octal_to_string(600)) # Should be rw--


discussion
r = 4
w = 2
x = 1
use tuple, string; will start as empty, list comprehension, for loop, list
'''
def octalToString(number):
    ''' function that changes permisions from
    
    octal integers to strings
    '''
    string = ''
    octal_letter = [(4,"r"),(2,"w"),(1,"x")] #defining a list of tuples octal_letter
    #mapping the permission values to their corresponding letters
  # Iterate over each of the digits in number
    for i in [int(n) for n in str(number)]:
    # Check for each of the permissions values
     for value, letter in octal_letter:
        if i >= value: #if th numer digit is greater than or equal to the permission value,
            # the corresponding letter is added to the string
            string += letter
            i -= value
        else:
            string += '-'
    return string


print(octalToString(777)) #rwx-rwx-rwx

'''
OR
'''
def octal_to_string(numbers):
    """
    Function that converts octal number permissions to string format
    """
    string = ''
    octalDict = {4: 'r', 2: 'w', 1: 'x'}
    for x in str(numbers):
        octalValue = int(x)
        for value, letter in octalDict.items():
            if octalValue >= value:
                string += letter
                octalValue -= value
            else:
                string += '-'
    return string

print(octal_to_string(777)) #rwx-rwx-rwx
