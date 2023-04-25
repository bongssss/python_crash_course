
# write a program that takes a value from a user 
#and only ends the program when the user gives a value between 18 and 23, both inclusive


#solution

# while(True):   
  #  number = int(input('Number: '))
   # if 18 <= number and number <= 23:
       
    # print('you have hit the jackpot')
     # break




# for loops
'''
range() function creates a sequence that can also be called an iterable
it takes 3 arguments namely:
- start: determines where the sequence starts, default value is always 0
- stop: determines the end of a sequence, 
it is usually one less than the given value i.e if given 5, stop value will be 4
-step : determines  the rate of increment in the sequence, default value for step is 1
you can give one two or all three arguments
 - 1 arg is considered as the stop value
 - 2 arguments are considered as start and stop respectively
 - 3 arguments are start, step and stop 
'''





'''
example
for number in range(6): # 1 argument = stop value
   print(number)
print('----------------2 arguments---------------')
for number in range (1,6): # 2 arguments = start and stop with step value of 1
   print(number)
print('-----------3 arguments------------------')
for number in range(1,7,2): # 3 arguments with start, stop, step
   print(number)
'''
# classwork
   #write a program that calculates the square of a number by repetitive addition

number =int(input('Number: '))
square = 0
for value in range(number ):
    square = square + number
    print('The square of',number, 'is', square)
    
    
  

    
    