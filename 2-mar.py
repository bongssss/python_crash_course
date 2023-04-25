'''
Cotrol structures

A feature that allows you to  structure your  program to make certain types of decisions
this inclused the ability for your program to run based on certain conditions
'''

# IF statements
'''
Allows you to run a portion of your program only if a condition is met
'''
if(1 < 2):
   print('I know what am doing')

print('I am done wih the IF statement')

if(3 > 5):
   print('this is impossible')

'''
    example

    Ask a user for the following details;

    -Name
    -Sex
    -Age
    Tthen print a statement to the user telling his/her application status
    Only users that are younger than 18 will be accepted
    '''
name = input('Name: ')
sex = input('Gender: ')
age = int(input('Age '))
academic_status = input(' Highest educational degree attained:')
academic_status = academic_status.upper() # lower() is astingfunction that converts all letters to CAPITAl letters

if (age < 18 and sex == 'male'): #the condition must always be true/ tested for truthy
        print('Hello, ', name, 'your application has been accepted, ypu can now proceed')
else: #this will run if the condition is false 
     print('Sorry your application has beeen rejected, try again next time.')

if( age < 18):
     print('Hello, ', name, 'you are our frontdesk person.')
elif(sex == 'boy'):
     print('Hello, ', name, 'you are our cleaner')
elif(academic_status.upper() == 'SSCE'):
     print('Hello, ', name, 'you are our designer.')
else:
     print('Thankyou for applying.')


     '''
     Classwork

     A) write a program that reads an integer from a user and
     displays a message indicating if the integer is odd or even

     B) it s commonly said that one human year is equivalent to 7 dog years.
       Howerver,this coversion fails to recoginse that dogs reach adulthood in approx 2 years.
       as a result, some people believe it is better to count each of the first two human years a 10.5 dog years
       and then count each following year as 4 dog years

       write a proram that implements the conversion from human years to dog years,
         ensure it works for conversions under 2 human years and over same period
         you program should display an appropriate error message if the user enters a negative number

     '''

     #soluton
     #1
number = int(input('number '))

if(number % 2 == 0):
     print('this number is even')
else: 
     print('this is an odd number')


     #2

human_years = round(float(input('Number in human years ')), 1)
#dogyears = float()
#=dog_years = human_years * 10.5
#=dog_years2 = human_years + 21

if(human_years <= 2 and human_years > 0):
     dogyear = human_years * 10.5
     print( 'dog year is ', dogyear)

elif (human_years > 2):
       remainder = human_years - 2
       dogyear = (2 * 10.5) + (remainder * 4)
       print('Dog years are ', dogyear)


elif  human_years < 0:
     print('This is a negative number')
     

