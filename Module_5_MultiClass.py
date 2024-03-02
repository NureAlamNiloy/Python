class Student:

    def __init__(self,name,Currentclass,id):
        self.name = name;
        self.Currentclass = Currentclass;
        self.roll = id;
    def __repr__(self):
        return f'Student Name : {self.name}, Current Class: {self.Currentclass}, Student Id is = {self.roll}'



niloy = Student("Nure Alam Niloy", 13, 581567)
print(niloy)