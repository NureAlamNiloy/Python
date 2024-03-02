# Constructor in class

class Phone1:
    manufacture = "bangladesh";
    # Constractor 
    def __init__(self,owner,brand,sms):
        self.owner = owner;
        self.brand =brand;
        self.sms =sms;

myPhone = Phone1("Niloy", "SamSung", 23464526552);
print(myPhone.owner,myPhone.brand, myPhone.sms);


class shop:
    def __init__(self,byer):
        self.byer = byer;
        self.cart = [];

    def AddToCart(self,item):
        self.cart.append(item);

niloy = shop("Ami Niloy toi kiso koibi naki");
niloy.AddToCart("mobile");
niloy.AddToCart("Laptop");
niloy.AddToCart("Bag");
print(niloy.cart);

arafat = shop("Arafat");
arafat.AddToCart("tab");
arafat.AddToCart("admit");
arafat.AddToCart("churini");
print(arafat.cart);
    
