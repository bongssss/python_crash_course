''''
how to write programs
- using declarative knowledge; statements of fact 

- imperative knowledge; how to i.e use steps to build a program
'''

print('Hello world') #print funcion takes as an argument a string 'Hello world', the argument goes into the bracket

print(34)# this print function takes an integer/number argument

#print('Age:' + 21)

print('Age:', 24)

#comments in python;
#  lines of text that are not recognised as code, they help to explain code to anybody that is looking at the code.
#  they allow you to write descriptions in the code. 
# they are of two types;
#  single line comment; they are used to write brief descriptions, usually in a single line. 
# they usually started using the pound symbol or hashtag
'''
and block level comment;
this is used to write comments that span multiple lines and are generally more detailed
written between 6 double or single quotes
'''
'''
Python Syntax
The acceptable way of writting code with python
 
python language is made up of primitives such as;
a) operators:  -, +, *, /, % or modulo, // integer division
operators can be Logical or Arithmetic
b) Data types: integers, strings, floats, booleans, null/none
'''

print(23 + 23) #product is an integer
print(23 * 2) #product is an integer
print(15 / 3) #product is a float
print(15 /5.0)#product is a float
print(16 % 2) #returns the reminder of the division as an integer
print('hello' +' '+ 'World') #product is a new stringthis is also an example of concatenation 
#print('He' - 'a') #rpoduct is a typeerror
print('We' * 6) # product is duplicated by a factor of the multiple



'''
class work
write a python statement that will print  'Hello World <your name>
take note of the space 
use the + operator
'''

#solution
name = 'Ubongabasi'
print('Hello'+ ' '+ name)

#OR
print('Hello', name)
'''
write an expression that will display 
Age: 78
take note of the space 
you are to use the + operator
'''
#solution
age = 78
print('Age:', +  age )

#or 
print('Age:', age)
# or 
print('Age: ' + str(28))# str is a fuction that converts an integer called casting in python to a string 


#Name = input('What is my Name: ')
#Age = input('How old are you: ')
#print('My name is ' + Name + '.' ' And I am ' + Age + ' years old') 



'''
class work 3 

ask a user for his name and favourite number
multiply the number by 2 and print the person's name as much as the number typed myltiplied by 2
'''

number = int(input('input number: ' )) 
NAME = input('Input Name: ' ) 
print( NAME * number * 2)


