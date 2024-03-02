class Bank:
    def __init__(self,name,balance):
        self._name = name; # ekta underscore mane proceted
        self.__balance = balance;#private object 2 ta underscore mane privet

    def getBalance(self):
        return self.__balance; 
    def withdrow(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance -amount;
            return f'ne tor {amount} tk toi dor ';
        else: 
            return f"ja fokira eto tk nai"

Niloy = Bank("Niloy the boro vai", 5002345);
print(Niloy.getBalance());
print(Niloy.withdrow(453));