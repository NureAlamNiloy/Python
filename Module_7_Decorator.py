import math;
import time;
def Timer(fun):
    def innerFun(*args,**kwargs):
        start = time.time();
        
        print("Time Started")
        print(fun)
        fun(*args,**kwargs)
        print("Time Ended")
        end = time.time();
        print(f"Total time is = {end - start}")
    return innerFun;

@Timer
def Factorial(n):
    print("Factorial Started") 
    result = math.factorial(n)
    print(f"The Factorial of {n} is = {result}")

Factorial(1200)