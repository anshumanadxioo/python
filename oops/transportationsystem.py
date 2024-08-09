# 1.> design a   university transportation system 
class Vehicle:
    def __init__(self,type):
        self.__type=type
    def set_details(self,fuelType,capacity,speed):
        self.__fuelType=fuelType;
        self.__capacity=capacity;
        self.__speed=speed;
    def get_vechileType(self):
        return self.__type;
    def get_allDetails(self):
        return (f"***{self.__type}***"
                f"fuelType: {self.__fuelType}"
                f"capacity: {self.__capacity}"
                f"speed: {self.__speed}"
                 )
        
        
class VehicleRegistry:
    def __init__(self):
        self.__vehicles=[];
    def addVehicles(self,vehicle):
        self.__vehicles.append(vehicle);
    def get_allvehicledetails(self):
             print(('\n').join(vehicl.get_allDetails() for vehicl in self.__vehicles));

print(" ******transportation system design****** ")
print("List of avilable vechile:--");
vechile_arr=["Bus","Car","Motercycle"];
i=1;
for vechile in vechile_arr:
    print(f"{i}:-{vechile}");
    i+=1;
vechile_choice=int(input("Enter the vechile choice"));
my_vehicle=vechile_arr[vechile_choice-1];
vechile1=Vehicle(my_vehicle);
print(f"you have the vechile:-{my_vehicle}")
print("now set all the details of your vehicle:-")
vechile_fuel_type=input("fuel_type")
vechile_capacity=int(input("capaciy of vechile"))
vechile_speed=int(input("speed of the vechile"))

vechile1.set_details(vechile_fuel_type,vechile_capacity,vechile_speed);
registry=VehicleRegistry();
registry.addVehicles(vechile1);
# print(vechile1.get_allDetails())
registry.get_allvehicledetails();
print("****Thankyou for registring with us");
# vechile2=Vehicle("Bus")
# vechile2.set_details("Desiel",15,100);
# vechile3=Vehicle("motercycle");
# vechile3.set_details("petrol",2,200)
