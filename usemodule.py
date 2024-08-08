import calc
from functools import reduce
a=34; b=43;
c=calc.add(a,b);
print(c);
print(calc.multiply(a,b));
nums=[12,23,45,67,4,6,12,16,18];
even=list(filter(lambda x:x%2==0,nums));
print(even)
double_even=list(map(lambda x:x*2,even));
print(double_even);
sum=reduce(lambda x,y: x+y,double_even);
print(sum)
