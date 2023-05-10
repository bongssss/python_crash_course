'''
ABSTRACTION IN OOP
The process of handling complexities by hiding unnecessary implementation details and showing the user only the 
essential features
ADVANTAGES
- allows user to understand complex objects easier by projecting their main features
- makes programs easier to maintain
- allows for easy reusability because oobjects that are easy to understand can be repurposed easily


REAL WORLD APPLCATION OF ABSTRACTION
- making and recieving payment via bank app
- moving a house fromthe blueprint to reality
- watching TV or netflix
* the common theme with these is that we dont know or care about what processes are involved in carrying
 out these things, we simply just do them with the resources and features provided to us.

PERFORMING ABSTRACTION IN PYTHON
We do so by using abstract classes and abstract methods to create instances 

an abstract method is a method contained in an abstract class, it si declared but ususally does not contain any
implementation i.e it is usually a function that returns nothing.

 a class containinng abstract methods is called an abstract class, it is usually a parent class or base class i.e
 it contains other classes called subclass(es)
imagine a class called 'shape' that contains subclasses like triangle, rectangle, square, etc this 'shape' class
is called an abstract class.

the subclasses like suqare and rectangle, will need methods in order to be able to compute their area 
and perimeter, but the methods will have to be unique to the shape.
this means that the area and perimeter methods are abstract methods as they will be contained 
in the class 'shape', remember tht abstract methods usually dont return an output.
the subclasses rectangle and square can override these abstract methods by calling them using inheritance
 and defining their own implementation of the methods area and perimeter using polymorphism. 

 keywords:  subclass, abstract method, abstract class, parent class, abstract class, base class,
 __init__: costructor method fo a class called everytime an object is created

 EXAMPLE DEMONSTRATED BELOW

'''
#example for the __init__ method
class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
         return True
        else:
          return False
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 = Student("Harry", 85)
print (student1.name)
print (student1.marks)
did_pass = student1.check_pass_fail()
print(did_pass)
print('-----------------------------------------------')
print('-----------------ABSTRACTION EXAMPLE-----------')

class Shape:
   '''
   this is the shape abstract class
   '''
   #area abstract method returns nothing, hense the pass statement
   def area():
      pass
   #perimeter abstract method returns nothing, hense the pass statement
   def perimeter():
      pass
   #square subclass
class Square(Shape):
   '''
   
   '''
   def __init__(self, length):
      self.__length = length
    #square area
   def area(self):
      return self.__length * self.__length
   #square perimeter
   def perimeter(self):
      return 4 * self.__length
   

   #rectangle subclass
class Rectangle(Shape):
   '''
   
   '''
   def __init__(self, length, breadth):
      self.__length = length
      self.__breadth = breadth
    #area function
   def area(self):
      return self.__length * self.__breadth
   # perimeter function
   def perimeter(self):
      return (self.__length + self.__breadth) * 2
   

square1 = Square(5)
Area = square1.area()
Perimeter = square1.perimeter()
print('SQUARE')
print(Perimeter)
print(Area)
print('-----------------------------------------')

rectangle1 = Rectangle(4,2)
Area = rectangle1.area()
Perimeter = rectangle1.perimeter()
print('RECTANGLE')
print(Perimeter)
print(Area)


