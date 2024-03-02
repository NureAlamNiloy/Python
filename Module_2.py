# Function in Python 
def Niloy(x,y):
    return x+y;

total = Niloy(3,6);
print(total);



# Local and global variable in python

balance = 7000;

def byThinks(item, price):
    global balance;
    balance = balance-price;
    print("balance after by item ",balance);

byThinks("chosma", 300);


#Built in function in python
higest = max(34,56,234,56,76,2342,56);
smallest = min(34,56,234,56,76,2342,56);
count = len([34,34,34,23,345,45,3,45,345])

print(higest);
print(smallest);
print(count);

#Multiple Return in python
def sum(x,y):
    result = x+y;
    multi = x*y;
    vag = x/y;
    rimender = x%y;
    return result,multi,vag,rimender;
    #return [result,multi,vag,rimender];

everything = sum(45,12);
print(everything);















