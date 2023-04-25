totalprice = float(input('Total invoice amount$: '))
tip = 0.05 * totalprice
cash = float(input('Amount in cash$: '))
card = float(input('Card payment$: '))
bankcharges = 0.04  * card
  


change = ((cash + card) - totalprice)  - bankcharges

if change < 0:
    outstanding = totalprice - (card + cash)
    print(f'Outstanding amount to be payed is ${outstanding}')
else:
    print(f'change to be returned to customer is ${change}')






'''#INT2HEX
def dec_to_hex(dec_num):
    """This program converts a decimal(base10) number to a hexadecimal(16)."""

    # Print the decimal value.
    print('Decimal:', dec_num)

    # Variable to store the hexadecimal output.
    hex_num = ''

    if dec_num == 0:
        print(dec_num)

    # While loop for division of dec_num by 16 until it is equal to zero.
    while dec_num > 0:

        # Remainder of divisions by 16.
        remainder = dec_num % 16

        # 10, 11, 12, 13, 14, 15 are A, B, C, D, E, and F respectively in hexadecimal.
        if remainder == 10:
            remainder = 'A'
        elif remainder == 11:
            remainder = 'B'
        elif remainder == 12:
            remainder = 'C'
        elif remainder == 13:
            remainder = 'D'
        elif remainder == 14:
            remainder = 'E'
        elif remainder == 15:
            remainder = 'F'

        # This stores the remainders in reverse order to give us our hexadecimal output.
        hex_num = str(remainder) + hex_num

        # We assign dec_num to have the value of the quotient of the division, before another division occurs again.
        dec_num = dec_num // 16

    # Print the hexadecimal value.
    print('Hexadecimal:', hex_num)


# User input
print(' Decimal to Hexadecimal '.center(40, '*'))
user_input = int(input('Enter the decimal number you want to convert to hexadecimal: '))

# Function call.
dec_to_hex(user_input)






    # Creating the Dictionary  
dictionary_hexa_to_decimal = {'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10 , 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}  
hexadecimal_string = input("Please enter the hexadecimal value: ").strip().upper()  
decimal = 0  
      
length = len(hexadecimal_string) -1  
       
for digit in hexadecimal_string:  
        decimal += dictionary_hexa_to_decimal[digit]*16**length  
        length -= 1  
       
print ("The converted hexadecimal string into decimal string is: ", decimal)  
'''

 



'''
write a program that creates a dictionary count of all items in a list
'''
colours = ['red', 'blue', 'green', 'yellow', 'green', 'red', 'blue', 'purple', 'orange']
cdict = {}
for color in colours:
    if color  in cdict:
        cdict[color] += 1
    else:
        cdict[color]= 1
print(cdict)


#example is a function for counting how many times each letter occurs in a piece of text
#the result is a dictionary where the keys are each letter in the present string
#and the values are howmany times each letter is present
String= input('input a string: ')

letter_dict = {}
for letter in String:
    if letter != ' ' and letter not in letter_dict:
        letter_dict[letter] = 1
    elif letter != ' ':
        letter_dict[letter] += 1 
print(letter_dict)
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
r = 4
w = 2
x = 1
'''

def octalToString(number):
    string = ' '
    octval = [(4,'r'), (2,'w'), (1,'x') ]
    for i in [int(a) for a in str(number)]:
        for value, letter in octval:
            if i >= value:
                string += letter
                i -= value
            else:
                string += '-'
    return string
print(octalToString(755))

def octString(normal):
    string = ''
    octval = {4:'r', 2:'w', 1:'x'}
    for x in [int(a) for a in str(normal)]:
        for key, value in octval.items():
            if x >= key:
                string += value
                x -= key 
            else:
                string += '-'
    return string
print(octString(755))

#4th APRIL.PY create a function that counts the number of words in a string and 
# returns each letter of the string and their index in tuples in a list
def countTuple(string):
 string = 'innovation'
 
 return [n for n in enumerate(string)]
  
 
print(countTuple('innovation'))

print('-------------------------------------------------------------------------------')
#OR  

def count_tuple_list(string):
    return [(a,b) for (a,b) in enumerate(str(string))]
print(count_tuple_list('Ubongabasiebongetim'))


'''
write a function that returns true if the first letter of the string 
is the same as the last letter of the string, false if theyre different
'''
word = str(input('any word at all: '))
def firstEqualsLast(word):
    if word == '' or word[0] == word[-1]:
        return True
    else:
        return False
print(firstEqualsLast(word))