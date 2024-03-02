class User:
    def __init__(self,name,age,money):
        self._name = name;
        self._age = age;
        self.__money = money;
    
    @property #getter without any setter its only radyable 
    def age(self):
        return self._age;
    @property #getter without any setter its only radyable 
    def salary(self):
        return self.__money;
    @salary.setter
    def salary(self,value):
        if value < 0:
            return "negative hoiya gese reeeeeeeeee";
        self.__money +=value;
        
samsu = User("copaaa",21,10000);
print(samsu.age);
print(samsu.salary);
samsu.salary = 45;
print(samsu.salary);












