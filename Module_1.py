""" 
print items in same line
1. print(n,end=" "); 

"""

name = input("Enter your name = ")
age = int(input("Enter your age = "))
roll = int(input("Enter your roll = ")) #input ee sob string hisabe ney tai type convert kora lage

text = f"Name is {name} roll {roll} age is {age}" # F string
print(text)
print(type(name)) # Kon type er variable taa janar jonno type() function use hoy

# Condition in python
if age > 10 :
    print('Good boy')
elif age > 20:
    print('Good beta')
else:
    print('Toi ja vag ante')


# while Loop in Python
num = 1;
while num: 
    num+=1;
    if num%2 == 1:
        continue;
    if num == 10:
        break;
    print(num);

#For loop in Python
numbers = [21,234,345,56,76,768,34];
sum = 0;
for i in numbers:
    print(i, "index is = ", numbers.index(i)); # index() function is use for find index of an element in array
    sum+=i
print("The sum is = ", sum);


for i in range(0,100):
    print(i);

"""


 ALT + Shift + A dile multi line comment kora jay

 othoba 3 ta kore dobule cotetion day multi line comment kora jay


 """

