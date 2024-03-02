
class Person:
    def __init__(self,name,age,hight,weight):
        self.name = name
        self.age = age
        self.hight = hight
        self.weight = weight;
    def eat(self):
        print("Vat mangso kha");

class Cricketer(Person):
    def __init__(self,name,age,hight,weight,team):
        self.team = team;
        super().__init__(name,age,hight,weight);
    def eat(self):
        print("vagetables kha");
    def __add__(self,other):
        return self.hight + other.hight;
    def __mul__(self,other):
        return self.age + other.age;
    def __len__(self):
        return self.weight;


Sakib = Cricketer("Niloy",35,65,34,"German");





