from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop:
    def process(self):
        print("calling from the laptop")
# obj=Computer();
# obj.process();
lap=Laptop();
lap.process();

