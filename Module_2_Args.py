# Args in python(joto iccha paramitter neya jabe ekta function ee)  
def Args(*number): 
    print(number);
    sum = 0;
    for num in number:
        sum+=num;
    return sum;

print(Args(1,2,3,4,5,6,7,8,9));

def argsPy(x,y,*z):
    sum = x+y+z[1];
    return sum;

print(argsPy(3, 4,4,2))


# kargs in function

def fullName(first,last,**title):
    name = f'full name is = {first} {last} {title}';
    for key,value in title.items():
        print(key,value);
    return name;

print(fullName(last = "Niloy", first = "Nure Alam",title="Sarkar",title2="Sarkar2",title3="Sarkar3"))




