class Soping:
    def __init__(self,name):
        self.name = name;
        self.cart = [];

    def AddToCart(self,item,price,quantity):
        product = {"item" : item, "price": price,"quantity":quantity};
        self.cart.append(product);
    def checkOut(self,amount):
        total = 0;
        for item in self.cart:
            total = item["price"]*item["quantity"];
        print(total);
        if amount < total:
            return f'Please Provide {total - amount}'
        else:
            return f'Your extra money {amount-total}'

Niloy = Soping("Ami  Niloy Cinos na amare ");
Niloy.AddToCart("Muri", 100, 2);
Niloy.AddToCart("Chira", 300, 3);
print(Niloy.cart);
print(Niloy.checkOut(7000))