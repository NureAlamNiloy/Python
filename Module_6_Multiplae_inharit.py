class family:
    def __init__(self,address):
        self.address = address;

class School:
    def __init__(self,name,level,id):
        self.name = name;
        self.id = id;
        self.level = level;

class Sports:
    def __init__(self,game):
        self.gameName = game;

class Student(family,School,Sports):
    def __init__(self, address,id,level,game,name):
        School.__init__(self, name, level, id)
        Sports.__init__(self, game)

