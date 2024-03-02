
# List oparetion in python

numberList = [342,43,23,3,6,7,2,78,23,678,2,743,124,8];
# print(numberList[start : end])
print(numberList[0 : 9])
# print(numberList[start : end : step])
print(numberList[0 : -1 : 3])
print(numberList[-1 : 2 : -1])
print(numberList[:])#print all valus 
print(numberList[::-1])#print all valus in reverse 
numberList.append(34532423);
print(numberList);
if 2 in numberList:
    numberList.remove(2);#remove a item from list
print(numberList);
numberList.insert(6,23462345234); # insert number 
print(numberList);
numberList.pop();
print(numberList);
numberList.sort();
print(numberList);
