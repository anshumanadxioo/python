# 1. ...................
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ");
#     print(" ")
    
# 2........................

# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ");
#     print(" ");

# 3........................

# for i in range(5):
#     x=1;
#     for j in range(i+1):
#         print(x,end=" ");
#         x+=1;
#     print(" ")

# 4.........................
# xfour=1;
# for i in range(5):
#     for j in range(i+1):
#         print(xfour,end=" ");
#     xfour+=1;
#     print(" ");

#5..........................
# for i in range(5):
#      for j in range(5,i,-1):
#          print("#",end="")
#      print(" ")

# 6...........................
# for i in range(4):
#     for j in range(10):
#         if (j>=4-i and j<=4+i):
#             print("#",end=" ");
#         else :
#             print(" ",end=" ")
#     print(" ")

#7.............................

# for i in range(5):
#     for x in range(i+1):
#         print(" ",end=" " );
#     for y in range(9-2*i):
#         print("#",end=" ");
#     for z in range(i+1):
#         print(" ",end=" ");
#     print(" ")

#8 .............................

# for i in range(9):
#     if(i<10/2):
#         for x in range(i+1):
#             print("#",end=" ");
#         for y in range(4-i):
#             print(" ",end=" ");
#         print(" ")
#     else :
#         for z in range(9-i):
#             print("#",end=" ");
#         for a in range(4-i):
#             print(" ",end=" "); 
#         print(" ")
    
#9..............................
# pos=1;
# for i in range(5):
#     internalpos=pos;
#     for a in range(i+1):
#         print(internalpos,end=" ");
#         internalpos=1 if internalpos==0 else 0;
#     for b in range(4-i):
#         print(" ",end=" ");
#     pos= 0 if pos==1 else 1;
#     print(" ")
# 10.............................
# ch='A'

# for i in range(5):
#    for a in range(4-i) :
#       print(" ",end=" ") 
#    for b in range(2*i+1):
#         print("*",end=" ")
#    for c in range(4-i):
#         print(" ",end=" ")     
#    print(" ")
# check weather the number is prime or not
# from math import sqrt
# def isPrime(num):
#    cnt=0;
#    for i in range(2,int(sqrt(num)),1):
#        if (num%i==0):
#           cnt+=1
#           if((num/i)!=i):
#               cnt+=1
#    if cnt<2:
#        return True;
#    else:
#        return False;

# if(isPrime(142)):
#     print("prime");
# else:
#     print("not prime")

# from array import *
# vals=array('i',[3,4,5,6,7]);
# newArr=array(vals.typecode,(a*a for a in vals))
# for x in newArr:
#     print(x, end=" ");
    
from numpy import *
# vals=array([23,43,23,12,32,21]);
# for x in vals:
#     print(x)
# arr1=array([2,4,6,8,9]);
# # arr2=arr1;
# arr2=arr1.view()
# arr1[1]=34
# for x in arr2:
#     print(x,end=" ");
    
# arr1=array([[2,3,4,5],[4,5,6,7]]);
# print(arr1.max())
# for x in arr1:
#     print(x,end=" ")
# m1=matrix('1 2 3 ; 4 5 6 ; 23 45 32')
# m2=matrix('4 3 8 ;12 34 54; 9 8 7');
# m3=m1*m2
# print(m3.shape)
# print(m1.max());


# sum two number without using the sum operation

# def sumNum(a,b):
#     ttl=0;
#     i=0;j=0;
#     while a:
#         digit=a&1;
#         a>>=1
#         ttl+=digit*int(pow(2,i));
#         i+=1;
        
#     while b:
#         digit=b&1;
#         b>>=1
#         ttl+=digit*int(pow(2,j));
#         j+=1;
#     return ttl;
   
        
# print(sumNum(11,5))


# def myfunction(a,*b):
#     for ele in b:
#         a+=ele;
#     return a;
# print(myfunction(43,1,2,3,4,5,6))

# def function2(a,**b):
#     for key,value in b.items():
#         print(key,value);
        
# val=function2('anshuman',caste="mishra",age=23,address="purwara")
# print(val)

##...............global and the local variables
# a=10;
# def something():
#     # global a
#     x=globals()['a']
#     a=5;
#     print(a,"inside",x);
# something()
# print(a,"outside")

##..................fibonacii series
# def printfebonaci(n):
#     a=0; b=1;
#     print(a);
#     print(b);
#     for i in range(2,n):
#        c=a+b
#        a=b;
#        b=c;
#        print(c)
       
# febo=printfebonaci(8);
# print(febo)

# def febonacii(n):
#     if n==0: return 0;
#     if n==1: return 1;
#     return febonacii(n-1)+febonacii(n-2);
    
    
# print(febonacii(6));

# def factorial(n):
#     if n==0|n==1 : return 1;
#     return n*factorial(n-1);
# print(factorial(5))

# lambda function ...................

# fun =lambda a,b:a*b
# res=fun(3,4);
# print(res)


#map filter reduce ...................
nums=[12,34,33,43,45,5,7,9,11,13,32]
# 1.> filter.......................
# def iseven(n):
#     return True if n&1==0 else False
# even=list(filter(iseven,nums));
# even=list(filter(lambda x:x&1==0,nums))
# print(even)

# 2.> map...........................
# def is_double(n):
#     return n*2;
# doub=list(map(is_double,nums));
# doub=list(map(lambda x:x*2,nums));
# print(doub);

# 3.> Reduce........................
from functools import reduce
# def is_Reduce(a,b):
#     return a+b;
# val=reduce(is_Reduce,nums);
# val=reduce(lambda a,b:a+b,nums);
# print(val);

    
    