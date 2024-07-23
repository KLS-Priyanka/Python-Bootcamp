# pattern printing
r=int(input("enter the rows"))
for i in range(1,r+1):
    for j in range(1,r+1):
        if i==j:
            print(" ",end=" ")
        print("*",end=" ")
    print()