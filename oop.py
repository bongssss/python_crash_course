'''
OOP serves to group functions together
under OOP we have class,objects, inheritance, polymorphism, etc
to declare a class ; use the class keyword.
classes start with a capital letter
dot notation helps you acess any of the abilities in the class


'''
class Apple:
    pass
class Apple1:
    color = ' '
    flavour = ' '
    size =  ' '


#creating a new instance of the apple class and assigining it to a variable creates an object

jonagold =  Apple1()
reddjango = Apple1()
# setting the values of the attributes using dot notation
jonagold.color = 'red'
jonagold.flavour = 'sweet'
jonagold.size = '12mm'

#retrieving class properties is done by using dot notation
print(jonagold.color)
print(jonagold.color.upper())
print(jonagold.flavour)
print(jonagold.size)
print('----------------------------------------------------------------')
#create another instance of apple class with different values
golden = Apple1()
golden.color = 'yellow'
golden.flavour = 'soft'

'''
class instance
we use methods to do stuff and perform actions
methods are functions that operate on the attributes of a specific instance
of a class

calling functions on ojects ececutes functions that operate on attributes of a specific instance
of the class

calling a method on a list only modifies the instance of a listand not all lists globally

instance methods take a parameter called 'self' which represents the instance the method is executed on

variables that have diffrernt values for different instances of the same class are called instance variables
'''

class Human:
    height = 182
    def speak(self):
        print('hello, world')

#create an instance or object of the class
sucess = Human()
sucess.speak()
print(sucess.height)
sucess.name ='sucess'  #usually not right
print(sucess.name)
print('-----------------------------------------------')



#example1
'''
a dog with class dog_years that determines the age of a dog
(one human year is 7 dog years)
'''
class Dog:
    age = 1
    def dog_year(self):
        self.age = self.age * 7

    def assign_age(self, age):
        self.age = age


dog1 = Dog()
print(dog1.age)
dog1.dog_year()
print(dog1.age)
dog1.assign_age(8)
dog1.dog_year()
print(dog1.age)