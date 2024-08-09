class School:
    name="einstein"
    age=23;
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def get_name(self):
        return (f"{self.fname} {self.lname}")
    @classmethod
    def clsmethod(cls):
        return cls.name
    @staticmethod
    def  changeage(ag):
        School.age=ag
obj=School("anshuman","mishra");
print(obj.get_name());
print(School.clsmethod())
# School.changeage(34);
obj.changeage(24)
print(obj.age)
        