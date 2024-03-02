class Shopping:
    cart = []; # Class Attribute ba static attribute
    origin = "German";
    def __init__(self,name,location):
        self.name = "Ekta name"; #
        self.location = location;
    def product(self,item,price,amount):
        remaining = amount - price;
        print(f'Item {item} price is {price} and the remaining = {remaining}');
    
    @classmethod #Class method aita direct use kora jay;
    def hudaiDakhi(self,name):
        print("hudai dekhi ki kormo tk nai");
    
    @staticmethod #aitake sorasori use kora jay self er na dileoo problem hoy naa
    def multi(a,b):
        print(a*b);


Shopping.hudaiDakhi("lungi");
Shopping.multi(23,34)



