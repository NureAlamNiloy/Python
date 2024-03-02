""" 



"""

class Animal:
    def __init__(self,name):
        self.name = name;
    def makeSound(self):
        print("Animal Makes some sound");

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name);
    def makeSound(self):
        print("meow meow");
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name);
    def makeSound(self):
        print("geow geow")

class goat(Animal):
    def __init__(self, name):
        super().__init__(name); 


Don = Cat("Don is Don");
Don.makeSound();
hutta = Dog("Ami deshi kutta");
hutta.makeSound();
less = goat("Goragori Khay");
less.makeSound();





