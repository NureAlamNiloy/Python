""" 
Python e caile amra ekta function er bitore arekta inner function declear korte pari ...
a

"""

def doubleDaker():
    print("aita main function taaa");
    def innerFun():
        print("this is inner function");
        return "ami sei inner function"
    return innerFun;

print(doubleDaker());
print(doubleDaker()());



def DoSomthing(work):
    print("work Started");
    work();
    print("work ended");
def coding():
    print("Coding in python");

print(DoSomthing(coding))
