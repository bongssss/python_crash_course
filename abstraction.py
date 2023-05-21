'''
some important OOP concepts:
CLASS
A class is used to create user-defined data structures in Python. 
Classes define functions, which are also called methods,
that describe the behaviors and actions that an object/instance created from a class can perform.

Classes aim at creating a blueprint or a design of how anything concept should be defined or look like.
 It defines what properties or functions that any object/instance which is derived from the class should have.

 I.E in a human class there weill be attributes or characteristics like name, age, gender, height and 
 methods like language, walk, sleep, greet, etc

 The properties that all Human objects must have should be defined in a method called init(). 
 Every time a new Human object is created, __init__() initializes each new instance of the Human class.
 class attributes are usually the same for all instances while instance attributes that are defined in the init 
 function are usually not the same across instances

 METHODS
 a method is a function defined within a class that can be called only from instances of that class. 
Like init() method, a method's first parameter is always self




INHERITANCE
Inheritance is the process by which a class can inherit or derive the properties(or data) and methods(or functions) of another class. 
Simply, the process of inheriting the properties of a parent class into a child class is known as inheritance.

Super()
The super() function in python is a inheritance-related function that refers to the parent class.
 We can use it to find a method to be used in the child class from superclass.
We write the super() keyword followed by the method name we want to refer from our parent class.

class Human:
    
    *def dance(self):*
        print("I can dance")
        
class Girl(Human):
    def dance(self):
        print("I can do classic dance")
    def activity(self):
       * super().dance()*

Here, we have defined the dance() method in Human and Girl classes. But, both methods have different implementations as you can see. In Human class,
 the dance method says "I can dance", whereas in Girl class, the dance method says "I can do classical dance"
 (polymorphism).

 POLYMORPHISM
 Polymorphism in OOPS refers to the functions having the same names but carrying different functionalities.
 Or, having the same function name, but different function signature(parameters passed to the function).

 i.e in the example above the  dance function appears twice (is polymorphic) (without the super function) 
 but does not have the same impementation i.e (prints different outputs)

 Polymorphism with Inheritance
It is possible to modify a method in a child class that it has inherited from the parent class, 
adding its own implementation to the method. 
This process of re-implementing a method in the child class is known as Method Overriding 
an example is seen in the human class example with the dance function



ENCAPSULATION
In other words, encapsulation is a programming technique that binds the class members 
(variables and methods) together and prevents them from being accessed by other classes.
 It is one of the concepts of OOPS in Python.
Encapsulation is a way to ensure security. It hides the data from the access of outsiders.

Getters and Setters
We can perform encapsulation by defining getter and setter methods for our classes. 
If anyone wants some data, they can only get it by calling the getter method.
 And, if they want to set some value to the data, they must use the setter method for that, 
 otherwise, they won't be able to do the same.
 But internally, how these getter and setter methods are performed remains hidden from the outside world.

 class Library:
    def __init__(self, id, name):
        self.bookId = id
        self.bookName = name
        
    def setBookName(self, newBookName): #setters method to set the book name
        self.bookName = newBookName
        
    def getBookName(self): #getters method to get the book name
        print(f"The name of book is {self.bookName}")

In this example, we defined the getter getBookName() and setter setBookName() 
to get and set the names of books respectively. 
So, now we can only get and set the book names upon calling the methods,
 otherwise, we cannot directly get or modify any value. 

Access Modifiers
Access modifiers limit access to the variables and methods of a class. 
Python provides three types of access modifiers private, public, and protected.

Public Member: Accessible anywhere from outside the class.
Private Member: Accessible only within the class
Protected Member: Accessible within the class and it's sub-classes
Single underscore _ represents Protected class. Double underscore __ represents Private class.
EXAMPLE
class Employee:
    def __init__(self, name, employeeId, salary):
        self.name = name    #making employee name public
        self._empID = employeeId  #making employee ID protected acessible within employee class and subclasses
        self.__salary = salary  #making salary private accessible within employee class only

      def getSalary(self):
        print(f"The salary of Employee is {self.__salary}")

the employee's name public, employee's ID protected, and the employee's salary private. 
Suppose we try to print all the values. 
Now, we will be able to access the employee's name or his ID, but not the salary(because it is private).
We can access private members from outside of a class by creating public method/getter method
 to access private members (just like we did above with getSalary()).
 


 




ABSTRACTION
Real lie example
when watching tv, the tv user only knows he/she may use the buttons on the remote to do it.
 What they don't know is how all this is happening internally, 
 for example how the tv sensor is capturing signals from the remote 
 and then how it is processing the received signals to perform the required action of changing the channel.


A good way to think of abstraction for a programmer is along side generalization.
 If, for instance, you wanted to create a program to multiply eight times seven,
you wouldn't build a function to only multiply those two numbers but you would build 
a function that is capable of multiplying any two numbers, making it more flexible, reusable
and more general purpose 

Achieving abstraction
in python abstraction can be achieved by creating abstract classes
in creating an abstract class in python,  we use the 'abc' abstract base class module
The term "abstract" refers to the fact that these classes are not meant to be instantiated directly 
but rather serve as a template for other classes while bas e simply implies that it is used to
provide a blueprint for  other classes
The 'abc' module provides the necessary tools for defining Abstract Base Classes (ABC)

to create an abstract class we use the following syntax:

from abc import ABC
class Newclass(ABC): # abstract class inherits ABC tools and features
  @abstractmethod    #decorator for indicating abstract methods
 def newmethod(self):
   pass   # for abstract mthods, implementation always varies for its subclasses ehnce no implementation is needed
# implementation must however be provided by each subclass

   
An abstract class can have both abstract methods and concrete methods.
methods that have the same implementation across all sublasses from the abstractclass are called concrete methods 
they usually have their implementation in the abstract class.  








'''
#EXAMPLE OF ABSTRACTION
from abc import ABC #IMPORT THE ABC FROM abc module
from abc import abstractmethod

#Abstract class
class Person(ABC):
    
    def __init__(self, name, age, gender, language, course): 
        '''
        __init__() initializes each new instance of this class.
       class attributes are usually the same for all instances while instance attributes that are defined
       in the init function are usually not the same across instances
        '''
        self.name = name
        self.age = age 
        self.gender = gender
        self.language =language
        self.course =  course

    def description(self):
        '''
        description is an example of a concrete method
        '''
        print(f'I\'m {self.name}, I\'m {self.age}, I speak {self.language}')
# ABSTRACT METHODS
    @abstractmethod
    def greeting(self): 
        pass

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def course_stud(self):
        pass


#SUBCLASS student
class Student(Person):
    def description(self):
        '''
        concrete method, remains the same across all subclasses
        '''
        return super().description()
    '''The super() function in python is a inheritance-related function that refers to the parent class.
 We can use it to find a method to be used in the child class from superclass.
We write the super() keyword followed by the method name we want to refer from our parent class.
'''
    
    def greeting(self):
        print(f'Bonjour, Je suis {self.name}')
    
    def speak(self):
        print(f'I speak {self.language}')

    def course_stud(self):
        print(f'I study {self.course}')
        
    
#new instance of student
new = Student('Ubong', 21, 'male', 'french', 'engineering')
new.description()
new.greeting()
new.speak()
new.course_stud()

print('-------------------------------------------------------------------------------------')


#SUBCLASS Professor
class Professor(Person):  
    '''
    inherits the person abstract class
    '''
    def description(self):  
        '''
        concrete method, remains the same across all subclasses
        '''
        return super().description() 
    '''The super() function in python is a inheritance-related function that refers to the parent class.
 We can use it to find a method to be used in the child class from superclass.
We write the super() keyword followed by the method name we want to refer from our parent class.
'''
    def greeting(self):
        print(f'Salut, mon nom est PROF {self.name}')

    def speak(self):
        print(f'I speak {self.language}')

    def course_stud(self):
        print(f'I dont study here, but I teach {self.course}')


#first instance of professor
first = Professor('Ekanem', 54, 'Male', 'French', 'maths')
first.description()
first.greeting()
first.speak()
first.course_stud()

