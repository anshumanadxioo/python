import time
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time();
#         res=func(*args,**kwargs);
#         end=time.time();
#         print(f"{func.__name__} ran in {end-start} time")
#         return res
#     return wrapper;
# @timer
# def example_function(n):
#     print("start..");
#     time.sleep(n)
#     print("end..")
# example_function(5);


# 2....................................................
def debugger(func):
    def wrapper(param,**params):
        res=func(param,**params);
        for ky,ind in params.items():
            print(f"{ky} and the value is:-{ind}");
        return res;
    return wrapper
@debugger
def greet(name,greeting="hello"):
    print(f"!{greeting} from {name}")
greet("anshuman",greeting="hanji")


