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

for i in range(9):
    if(i<10/2):
        for x in range(i+1):
            print("#",end=" ");
        for y in range(4-i):
            print(" ",end=" ");
        print(" ")
    else :
        for z in range(9-i):
            print("#",end=" ");
        for a in range(4-i):
            print(" ",end=" "); 
        print(" ")
    