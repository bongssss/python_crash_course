'''
Examples of string methods
'''


def initials(phrase):
    words = phrase.upper().split()
    initials = ''
    for word in words:
       initials += word[0]

    return initials
  
print(initials('local area network'))


'''
fromatting strings
we can use positional arguments to specify order
'''

# example with implicit argument

name = 'Ubong'
number = len(name)* 2
addy = '246, Ubong avenue'

print('hello {}, your lucky number is {}'.format(name, number))

print('hi {0}, your name is {1} characters long and {2}.'. format(name, number, addy)) 

# using positional arguments
print('example of a {1} character(s) long word is {0} at {2}.'. format(name, number, addy))


#another example of using the format method with keyboard argument
print('Your lucky number is {number}, {name}.'. format(name = name, number = len(name * 3)))


'''
exercise 

 the student_grade function uses the format mathod and returns the phrase 'X received Y% on the exam'
for example student_grade ('Reed', 80) should return 'Reed recerived 80% on an exam'

'''

def student_grade(name, grade):
    return '{} received {}% |in the exam.'.format(name, grade)


print(student_grade('Reed', 80))

print(student_grade('Paige', 93))
      
print(student_grade('Jesse', 85))




# another fromat method example, making a number print with 2 decimals

price = 7.5
with_tax = price * 1.09
print(price, 'and with tax', with_tax)


# this ine prints properly. the 2f means we format to 2 decimal places
print('base price ${:.2f}. with tax: ${:.2f}'.format(price, with_tax))


'''
modifying the  the celcius to print cleaner
 here the >3 operator is used to align text to the right, a total of 3 spaces
 the >6.2f operator is used to align text to the right to a total of 6 spaces and 2  decimal spaces
  the ^ operator is used to justify a string in a given space
  anything after the ':' is used to format the output of a string
'''
def tocelcius(x):
    return (x-32)*5/9


for x in range (0,101,10):
    print('{:<3.2f} F | {:>6.2f} c'. format(x, tocelcius(x)))

#exponent representation of a number 
print(' exponent representatation {0} is {0:e}'. format(1566.345))

#binary  representation 
print(' binary of {0} is {0:b}'.format(12))

# string alignment

print ("|{:<10} |{:^10}|{:>10} |". format ('butter', 'bread','ham' ))

# The replace method replaces the first matching word
print('Happy New Year'.replace("Happy", "Brilliant"))

# The join function join seperate words in sentence
list_of_words = ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
print(' '.join(list_of_words))

# The find function returns the index of the matching word

find_word = 'Happy New Year'

print(find_word.find('ew'))

# Formatted string literals
muscian = "Lucky" 
print (f'Hello {muscian:}')

item = "Green Cup"

amount = 5

price = amount * 3.25
224
print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')