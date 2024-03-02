# Dictionary.. it has 2 part key and value

person1 = {"name": "Niloy", "address":"Brahmanpara","age": 23}
print(person1);
print(person1["age"]);
print(person1.keys());
print(person1.values());
person1["name"] = "Sumo";
person1["address"] = "Cumilla";
print(person1);

# Dictinary looping
for key,value in person1.items():
    print(key,value);
