from abc import ABC, abstractmethod #abstruct base class

class animal(ABC):
    @abstractmethod  #enforce all derived class to have eat method
    def eat(self):
        print("I need Food");
    def move(self):
        pass

class monkey(animal):
    def __init__(self,name):
        self.name = name;
        super().__init__()
    def eat(self):
        print("oi method er kiso dekhay naa")

jony = monkey("Jony");
jony.eat();