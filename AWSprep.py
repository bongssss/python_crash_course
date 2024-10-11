class Car:
    def __init__(self, color, mileage):
        self.mileage = mileage
        self.color  = color
        
    def __str__(self):
        return(f'the mileage on the {self.color} car is {self.mileage} ')
        
        
        
        
        
car1 = Car(color="red", mileage= "20 thousand Miles")
car2 = Car(color="blue", mileage= "30 thousand Miles")

for car in (car1,car2):
    
    print(car)
    
print("-----------------------")  
print( car1, car2)
#print(f'the mileage on the {car1.color} and {car2.color} are {car1.mileage} and {car2.mileage} repsectively')



print('----------------------------')
# dog.py

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    
    
class GoldenRetriever(Dog):
    def speak(self, sound='Bark!'):
        return f"{self.name} says {sound}"
    #super().speak("Bark!")  # Calling parent class method
     
    
    
my_dog = Dog("Fido",4)
golden_retriever = GoldenRetriever("Max",9)

print(my_dog)
print(golden_retriever)
print(my_dog.speak("Woof"))
print(golden_retriever.speak())  

print('-------------------------------------------')
class Animal:
    def __init__(self, name) :
        self. name = name
    def make_sound (self) :
        pass
class Swimmable:
    def swim(self) :
        return f"{self.name} is swimming"
class Fish (Animal, Swimmable):
    def __init__(self, name) :
# Call the constructors of base classes
        Animal.__init__(self, name)
        Swimmable.__init__(self)
    def make_sound (self) :
        return "Screeeee ek ek ek.!"
# Create an instance of the FlyingFish class
flip = Fish("Flip")
# Access methods from different base classes
print(flip.make_sound())
print(flip.swim())


print('-------------------------------------------')
"""
class Animal:
    def __init__(self, name) :
        self. name = name
    def make_sound (self) :
        pass
class Swimmable:
    def swim(self):
        return f"{self. name} is swimming"
class Fish(Animal, Swimmable) :
    def __init__(self, name) :
# Call the constructors of base classes
        super().__init__(self, name)
        super().__init__(self)
    def make_sound (self) :
        return "Screeeee ek ek ek.!"
# Create an instance of the FlyingFish class"
flip = Fish("Flip") 
"""

print("-------------------------------------------------")

def mis(a,b):
    while b:
        a, b = b, a% b
    return a
res = mis(48,18)
print(res)
print("--------------")

num = [1,2,3,4,5]

for i in range(len(num)):
    if i % 2 == 0:
        num[i] *=2

print (num)
