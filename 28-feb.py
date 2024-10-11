'''
Variables in python
------------------------------------------------------------------------
A memory space allocated to store data.
different languages have different ways of assigning variables.

in python variables are crated by;
 typing a name and values are assigned using a single equal sign 

 Rules for variables in python
 -------------------------------------------------------------------------
 a) a variable name must start with either a letter or underscoore
 b) a variable cannot start with a number
 c) a variable can contain aplhanumeric charactersand underscores
 d) variable names are case sensitive
 e) it cannot be any of the python keywords
 '''

name = 'Ubongabasi'
print(name)

print(type(name))# prints the datatype of the variiable
print(type(56))
print(type(2.9))

first_name = ' snake_notation'
firstName = 'camelNotation'
FirstName = 'PascalNotation'



'''
Assignment
list all the python keywords you can possibly find
'''
age = int(input('How old are you? ')) #int() casts the string data type to integer
print(type(age))




'''
classwork

write a program that gets name, quantity sold, 
unit price and calculates the total price of goods sold.
 Then prints a meaningful sentence.
'''

#solution

Name = input('input your name: ')
quantity = input('Quantity of goods sold: ')
unitprice = input('unit price is: ')
totalprice = int(quantity)* int(unitprice)
#newprice = str(totalprice)
print('The number of goods sold is '+ quantity + ' sold at '  + unitprice + 
       ' per product. ''Total price is ' +str(totalprice))