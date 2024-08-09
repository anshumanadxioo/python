class Student:
    def __init__(self,m1,m2):
        self.m1=m1;
        self.m2=m2;
    def __add__(self,other):
        m1=self.m1+other.m1;
        m2=self.m2+other.m2;
        s=Student(m1,m2);
        return s;
    def show(self):
        print("show of parent is called")
    def mul(self,other):
        m1=self.m1*other.m1
        m2=self.m2*other.m2;
        s=Student(m1,m2);
        return s;
    def __repr__(self):
        return (f"student ({self.m1},{self.m2})")
    def __str__(self):
        return (f"studentstr ({self.m1},{self.m2})")
class Studentchild(Student):
    # pass
    def show(self):
        print("show of child is called")
s1=Student(34,45);
s2=Student(12,34);
# s3=s1+s2; 
s3=s1.__add__(s2)
s4=s3.mul(s2);
print(s3,"addition");
print(s4,"multiply");
s5=Studentchild(23,45);
(s5.show());
        