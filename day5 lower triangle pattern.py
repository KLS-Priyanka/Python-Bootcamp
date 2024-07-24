# r=int(input("enter the number"))
# for i in range (r):
#      for j in range(r-i):
#            print("*",end=(" "))
#      print( )



r=int(input("enter the number"))
for i in range (r+1):
     for j in range(r+1):
         if(i<j):
           print("*",end=(" "))
     print( )