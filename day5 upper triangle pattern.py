# upper triangle pattern
r=int(input("enter the number"))
for i in range (1,r+1):
     for j in range(i):
           print("*",end=(" "))
     print( )



r=int(input())
for i in range (r+1):
     for j in range(r+1):
         if(i>j):
           print("*",end=(" "))
     print( )