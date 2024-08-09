class Iterator:
    def __init__(self):
        self.__num=1;
    def __iter__(self):
        return (self);
    def __next__(self):
        if(self.__num<=10):
            val=self.__num;
            self.__num+=1;
            return val;
        else:
            raise StopIteration;
        
value=Iterator();
# for i in value:
#     print(i);
    
    
    # ..............................................
    # Generators
def inifinite_seq():
    num=0;
    while True:
        yield num
        num+=1;
seq=inifinite_seq();
print(next(seq));
print(next(seq));
print(next(seq));
print(next(seq));