from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,email,nid):
        self.name = name
        self.email = email
        self.__id = 123
        self.__nid = nid
        self.wallet = 0
    
    @abstractmethod
    def displayProfile(self):
        raise NotImplementedError
class Rider(User):
    def __init__(self,name,email,nid):
        super().__init__(name,email,nid);





