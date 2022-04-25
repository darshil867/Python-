from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('it\'s running')

class Whiteboard(Computer):
    def write(self):
        print('It\'s writing')

class Programmer:
    def work(self, com):
        print('Solving bugs')
        com.process()

# com = Computer()
# com.process()

com1 = Laptop()
com2 = Programmer()
com3 = Whiteboard()
com2.work(com3)