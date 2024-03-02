class Bank:
    def __init__(self,balance):
        self.balance = balance;
        self.minBalance = 100;
        self.maxBalance = 1000000;
    def getBalange(self):
        return self.balance;
    def diposit(self, amount):
        if amount > 0:
            self.balance += amount;
    def withdrow(self, amount):
        if amount < self.minBalance:
            return f'Fokira eto kom tk amra dei naa ja vag antee';
        elif amount > self.maxBalance:
            return f'Eto taka nai amader kase tore eto tk dite parmo naa';
        else:
            self.balance -= amount;
            return f'Here is your amount {amount} now your balance is {self.balance}'

BrakBank = Bank(15000);
print(BrakBank.withdrow(25));
print(BrakBank.withdrow(250000000));
print(BrakBank.withdrow(2500));



        