import time
#   case 1 timing function in decorator...............................
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


# 2..................debugger function in decorator..................................
# def debugger(func):
#     def wrapper(*params,**kparams):
#         params_val=(' ').join(str(val) for val in params );
#         print(params_val);
#         res=func(*params,**kparams);
#         kparams_val=(' ').join(f"{k}=={v}" for k,v in kparams.items())
#         print(kparams_val)
#         return res;
#     return wrapper;
# @debugger   
# def greet(*param,**params):
#     print("hello")
#     # param_val=(' ').join(str(val) for val in param);
#     # print(param_val);
#     # kyparms=(' ').join(f"{k}={v}" for k,v in params.items())
#     # print(kyparms)
# greet("nam","kam","sam",greeting="hello",meeting="bye");

# 3.....................cache return value function ........................................
import time
def cache(func):
    cache_value={};
    def wrapper(*params):
        if params in cache_value:
            return cache_value[params]   
        res=func(*params)
        cache_value[params]=res
        return res;
    return wrapper;
@cache
def long_running_fun(a,b):
    time.sleep(5);
    return a+b;
print(long_running_fun(3,4));
print(long_running_fun(5,6))
print(long_running_fun(3,4));

