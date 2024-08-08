class Car:
    ttlcar=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.ttlcar+=1;
    def greeting(self):
        print("hello")
    def fullName(self):
        return(f"{self.__brand} {self.__model}")
    def get_brand(self):
        return self.__brand+"!";
    def get_model(self):
        return self.__model+"!";
    def set_brand(self,newbrand):
        self.__brand=newbrand
    def set_model(self,newmodel):
        self.__model=newmodel;
    def fuel_type(self):
        return "petrol or desiel"
    @staticmethod
    def gen_Description():
        return "cars are means of transport";
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.__battery_size=battery_size
    def get_battery_size(self):
        return self.__battery_size;
    def fuel_type(self):
         return "electric power";
    
my_car=Car("tyota","corola");
# print(my_car.__brand)
# print(my_car.__model)
# print(my_car.get_brand());
# print(my_car.get_model());
# my_car.greeting();
# print(my_car.fullName());
# my_car.set_brand("hero");
# my_car.set_model("mx-100");
# print(my_car.fullName());
# print(my_car.fuel_type());
# print(my_car.gen_Description());   ye abb nahi chalega
print(Car.gen_Description());
e_car=ElectricCar("tesla","model s","85 kwh")
# print(e_car.get_brand())
# print(e_car.get_model())
# print(e_car.fullName());
print(e_car.fuel_type());
print(Car.ttlcar);
        