class Dog:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return print(f"my name is {self.name}")
        
        
        
dog1 = Dog('Peggie')
dog1name = dog1.getName()
print(dog1name)
