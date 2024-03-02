class BaseClass:
    def __init__(self,name,color,price):
        self.name = name;
        self.color = color;
        self.price = price;

    def move(self):
        pass
    def __repr__(self):
        return f'name is = {self.name}, price is = {self.price}';

class Bus(BaseClass):
    def __init__(self, name, color, price,seat):
        self.seat = seat;
        super().__init__(name, color, price);

class Truk(BaseClass):
    def __init__(self, name, color, price,weight):
        self.weight = weight;
        super().__init__(name, color, price);

class PickUp(Truk):
    def __init__(self, name, color, price, weight):
        super().__init__(name, color, price, weight);

class AcBus(Bus):
    def __init__(self, name, color, price, seat,tampar):
        self.tampar = tampar;
        super().__init__(name, color, price, seat)
        def __repr__(self):
            print(f'{self.seat}')
            return super().__repr__();


greenLine = AcBus("Green Line", "Green-White", 23145463455234, 50, 22);
print(greenLine);

