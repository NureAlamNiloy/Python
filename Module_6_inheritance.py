# inheritance

class Device:
    def __init__(self,brand,color,price):
        self.brand = brand;
        self.color = color;
        self.price = price; 
    def run(self):
        return f'Running = {self.brand}'

class Laptop:
    def __init__(self,memory,ssd): 
        self.memory = memory; 
        self.ssd = ssd
        
class Phone(Device):
    def __init__(self,brand, price, color, duelSim):
        self.duelSim = duelSim 
        super().__init__(brand,color,price)
    def phoneCall(self,number,text):
        return f'Sending SMS to {self.number}';
    def __repr__(self):
        return f'Id dule Sim {self.duelSim}'; 


myPhone = Phone("SamSung", 45645, "Blue", True)
print(myPhone.brand)




