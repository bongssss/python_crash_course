'''
Unexpected events occuring during execution of a program
AKA errors and they are raised or thrown by python code that encounters th error/unexoected circumstance

A raised error may be caught by a surrounding context that handles the exception in an appropriate manner
If uncaught, an exception causes the printer to to stop executiong th program and report the appropriate 
message to the console


#COMMON TYPES OF ERRORS
NameError: raised if a nonexistent identifier is used
TypeError: raised when a wrong datatype  is sent to a function
ValueError: raised when a parameter has an invalid value
ZeroDivisionError: raised when a division operator is used with 0 as a divisor


A ValueError is raised when the correct number and type of parameters are sent but the value is illegitimate
for the context of the function

Example: int('3.4') will throw a Valuerror because the value there does not represent an integer.
Python sequence types (e.g. list, tuple,str) raise an IndexError when syntax such as data[k] is used,
and the value of k is not a valid index of for the
given sequence. Sets and dictionary raise a KeyError when an attempt is made to access a nonexistent element.


# RAISING AN EXCEPTION
An exception is raised by executing the raise statement with an appropriate 
instance of an exception class as an argument that designates

'''

# int('3.5')
# data = 'sample keyerror'
# data[30]
# data = ['red', 'blue', 'yellow']
# data[8]

#raising an error
#raise ValueError('num cannot be negative')

#write a function that checks the validity of a variable
def validate(x):
    if not isinstance(x, (int, float)):
        '''isinstance() function returns True if;
         the specified object is of the specified type, 
        otherwise False.
        If the type parameter is a tuple,
        this function will return True if the object is one of the types in the tuple.
        '''
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')
    validate('a')
   
    '''
    checking the type and value of a variable demands additional execution time, if taken to extremes, 
    will be counter to conventional python

    '''

    #consider an example
    #write prgram that sums the collection of numbers
    import collections
    values = [4, 5, 7, 9]
    if not isinstance(values, collections.iterable):
        raise TypeError('values must be an iterable datatype')
    total = 0
    for v  in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric')
        total = total + v



