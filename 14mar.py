'''
FOR LOOP
we can loop; not only over numbers but also over other datatypes like strings, lists, tuples etc
'''

sports = 'my favourite sport is fishing.'

for letter in sports:
    print(letter, end='  ') #prints the string horizontally


stringlength = len(sports)# displays the length of the string index
print(stringlength)

#rewriting the for loop using a while loop
counter = 0
while counter < len(sports):
    print(sports[counter])
    counter  = counter + 1

stringlist =  sports.split(' ') #splits the sentence on every space to create a list
print(stringlist)

for word in stringlist:
    print(word.upper()) #prints in uppercase letters 


'''
write a program that asks a user for age and favourite word, 
tehn the program will print the users name, and cheer the favourite word the age number of times
'''

name = input('name: ')
age = int(input('age: '))
print(f'{name}, let me cheer your name {age} times')
faveword = input('favourite word: ')

count = 0
while count < age: 
    print( faveword)
    count += 1

'''
for word in range(age):
    print(faveword + '!!!')


'''


