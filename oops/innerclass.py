class Student:
    def __init__(self,name,rlno):
        self.__name=name
        self.__rlno=rlno
        self.lap=self.Laptop("hp","rt");
    def show(self):
        return (f"{self.__name}{self.__rlno}");
    class Laptop:
        def __init__(self,br,pro):
            self.brand=br;
            self.prcessor=pro
        def showlap(self):
            return (f"{self.brand} {self.prcessor}")
        
std1=Student("anshuman",23)


print(std1.lap.showlap());