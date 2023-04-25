'''
control structure --- LOOPS

a block of  code that repeats based on a set of conditions

there are two types of loops in .py
1) while
2) for

while loop: 
a structure that repeats a block of code until a certain condition is no maore met.
 You use the while loop when you dont have a pre-determined number of times you want to repeat a block of code 
with the whileloop you mustseta condition outside of the loop andensure it is changed within the loop
 
 
 for loop:
 a looping structure that runs until it gets to the end of a sequence .
   it is used when you have a pre-determined number of  times you want to run your loop
   the range() function is used together with the for loop together with the sequence needed bythe for loop
 '''

 #example

 #write a program that prints 'I am alive' until the value of age is greater than orequal to 85'


 #solution
age = 0
while (age <= 85):
    print('I am alive at', age)
    age += 1 # same as writing age = age + 1


    #write a program that prints all even numbers less than 50, 
    # if the number is 0 not considered as an even number, your program should print 0 
    # let your program print the last number in the loop with the loop statement,'the loop ends, lastnumber'
    # test your program with these numbers65, 74, 0,120,40,32

    #soln

number = int(input('number '))
count = 0 
while (count <= number):
    if(count != 0 and count < 50 and count % 2 == 0):
        print(count)
    count +=1
print('the loop ends, ', count)      

       
    

    
    