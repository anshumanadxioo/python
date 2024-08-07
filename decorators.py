import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time();
        res=func(*args,**kwargs);
        end=time.time();
        print(f"{func.__name__} ran in {end-start} time")
        return res
    return wrapper;
@timer
def example_function(n):
    print("start..");
    time.sleep(n)
    print("end..")
example_function(5);