""" 

list --> []
Set --> {}
Tuple --> ()

Set hocche unique items aikhane kono duplicate item thakbe naa

 """

numbers = [23,45,234,344,34,345,56,34,45,6,3,2,4,6,34,56];
print(numbers);
numbersSet = set(numbers);
print(numbersSet)
numbersSet.add(34567654321);
print(numbersSet);
numbersSet.remove(34);
print(numbersSet);



A = {1,3,4};
B = {1,2,3,4,5};
print(A & B);
print(A | B);