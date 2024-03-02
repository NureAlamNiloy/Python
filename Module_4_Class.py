# Class in python
class Phone:
    name = "Redmi Note 10";
    price = 22000;
    color = "Blue";
    feature = ["camara", "speaker","Display"];
    def call(self): #Python ee Class ee method declear kora hole delaful ekta perameter deya lage
        print("Calling Some one");
    
    def serve(self,phone,sms):
        text = f"number is:{phone} massage is : {sms}";
        return text;



myPhone = Phone();
print(myPhone);
print(myPhone.name);
print(myPhone.color);
print(myPhone.price);
print(myPhone.feature);
myPhone.call();
print(myPhone.serve(823789324, "I love u and I miss u"))




class Calclutor:
    brand = "Casio";
    def add(self,x,y):
        return x+y;
    def diff(self,x,y):
        return x-y;
    def multiply(self,x,y):
        return x*y;
    def divide(self,x,y):
        return x/y;


calcute = Calclutor();

print(calcute.add(4, 5));
print(calcute.diff(4, 5));
print(calcute.multiply(4, 5));
print(calcute.divide(4, 5));




