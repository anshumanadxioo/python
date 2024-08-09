class A:
    def __init__(self):
        print("calling the A");
    def feature1(self):
        print("call A feature");
        
class B:
    def __init__(self):
        print("calling the B");
    def feature2(self):
        print("feature of the class B");
class C(A,B):
    def __init__(self):
        super().__init__();
        print("calling the C ");
    def featureC(self):
        return super().feature2()
    
    
# obj1=A();

# obj1.feature1();
# obj2=C();
# obj2.feature1();
a='3'
b='4';
print(str.__add__(a,b));
