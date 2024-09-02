from abc import ABC, abstractmethod

class Human(ABC):
    @abstractmethod
    def get_name(self):
        return 'Name'
    
class Worker(Human):
    def get_name(self):
        return super().get_name()

w = Worker()
print(w.get_name())