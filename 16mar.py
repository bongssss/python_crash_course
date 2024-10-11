'''
FUNCTIONS

a function is a block of code that runs only when the function is called.
it must perform a single task and it must be clear
data known as parameteres are ususally passed into a function
it usually returns data as a result


- Advabtages
code readability and reusability 

-Types of functions
built in functions / library functions: standard functions available for use

user defined functions: functions ceated by the user to meet personal preference requirements 

'''

# creating a function: using the def keyword

def functionname():
    #statement
    #statement
    #pass
    return

'''
function parameters and arguments
 defining a function we use the term parameters and arguments are used when calling the function
can have any no of args seperated by a comma
must be called with the correct number of arguments i.e equal to amout of paras
to call a function use the function name  followed by open and closed braces()

types of function arguments

default args
keyword args (named, arguments)
positional args
abitrary args (*arg, **kwarg)
'''

#defining funcions with paras/parameters  and calling with args/arguments

def add(num1, num2):
    num = num1 + num2
    return num

#call function using args#arguments
num1, num2 = 5,23
result = add(num1, num2)
print(result)


# a function to check if a number is prime

def isprime(number):
    if number in [2,3]:
        return True
    if(number == 1) or (number % 2 == 0):
        return False
    r = 3
    while r * r <= number:
        if number % r == 0:
            return False
        r += 2
        return True
    

# call the function
primeresult = isprime(61)
print(primeresult)

'''
Docstring
the first string after a function is called a docstring
it is used to describe the functionality of the function
it is for optional use but is considered god practice
'''

# a function that checks if a number is odd or even using docstring

def oddOreven(num):
    '''
    function to check if a number is odd or even
    args:
    param1 : first param
    param2: second param
    num: is the number to be checked

    return:
      function returns sos and so

    raises: 
       typeeror: raises an exeption

    '''

    if num % 2 ==  0:
        print('even')
    else:
        print('odd')

# print the docstrin
print(oddOreven.__doc__)


'''
Anonymous function
 a function without a name is created using he lambda keyword
'''
# function that squares a num
squared = lambda x: x**2

def squared(x):
    return x**2





''' write a function; getseconds that calculates the amount of seconds in 2 hours and 30 minutes 
then add this number to the amount of seconds in 45 minutes and 15 seconds then print the result
     
    ans = 11715
    ''' 
def getseconds(hour, minute, sec):
    return 3600*hour + 60*minute + sec
time1 = getseconds(2, 30, 0)
time2 = getseconds(0, 45, 15)
totaltime = time1 + time2

print(totaltime)

