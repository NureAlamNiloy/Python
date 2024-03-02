class Book:
    def __init__(self,name):
        self.name = name;
    def read(self):
        raise NotImplementedError()

class Physics(Book):
    def __init__(self, name):
        super().__init__(name);
    def read(self):
        print("boi daa por");
    
topon = Physics("topon er boi niya ja");
topon.read();
print(issubclass(Physics,Book))



