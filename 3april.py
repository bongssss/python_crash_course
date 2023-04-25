
'''
There are many ways you can handle possible exception cases in your code.
For example, when performing a division operation x/y, 
there is a clear risk that a ZeroDivisionerror will be raised when variable y has a value o.
In an ideal situation, the logic of the program may dictate that y has a nonzero value, thereby. 
removing the concern for error. 
However, in complex situations or when the value of y depends on some external input,
there remains some possibility of an error.
One way to manage exceptional cases is to "look before you leap".
 This involves writing proactive conditional test logics in your program.
Another way, often used by professional Python programmers is 
"it is easier to ask for forgiveness than it is to get permission."
This philosophy means that we need not spend extra execution time safeguarding against every possible exception
 case as long as there is a mechanism for coping with the problem after it arises.
In Python, this philosophy is implemented using a try-except controi structure.
The "try" block is the primary code to be executed.
 Following the try-block are one or more "except"
cases each with an identified error type and an indented block of code.
'''

def division(a,b):
    if b == 0:
        ans = a
    else: 
        ans = a/b

    return ans
print(division(2,0))

#OR
def divide(x,y):
    if y == 0:
        print('you cant divide by this number')
    else:
        return x/y

x = int(input('x is: '))
y = int(input('y is: '))


#OR

c = int(input('enter value for c: '))
d = int(input('enter value for d: '))
if d != 0:
    ratio = c/d
else:
    print('Error message')


#OR
try:
    ratio =x/y
except ZeroDivisionError:
    print('error message')

#OR

try:
    fp = open('sample.txt') #may fail for some reasons
except IOError as e:
 print('Unable to open file', e) #e is an instance of the exception

#handling more than one type of exeption
age = int(input('age in years: '))
'''
the statement could fail for various reasons
 the call to input will raise an EOFError (End Of Line Error)if the console input fails
'''
age = -1
while age <= 0:
    try:
        age =int(input('enter your age in years: '))
        if age <= 0:
            print('your age must be positive')
    except ValueError as e:
        print('invalid response', e)
    except EOFError as e:
        print('an error occured while reading the text: ', e)
    finally:
        print('this program runs irrespective of anything')



'''
custom exceptions can br defined by creating a new class from the bultin python exception class
with the following syntax
'''
class CustomError(Exception):
    ...
    pass
try:
    ...
except CustomError:
    ...




# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")
