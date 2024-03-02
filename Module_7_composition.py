class Engine:
    def __init__(self):
        pass
    def start(self):
        print("Engine Starting")

class Driver:
    def __init__(self):
        pass

class Car:
    def __init__(self):
        self.engine = Engine();
        self.driver = Driver();
        
        
print(Car().engine.start());