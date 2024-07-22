
# n=int(input("enter the number"))
# c=0
# for i in range(1,int(n**0.5)+1):
#     if n%i==0:
#         c+=1
# if c==1:
#     print("prime")
# else:
#     print("composite")
    

n=int(input("enter the number"))
c=0
sq=n**0.5
if n==1:
    print("neither prime nor composite")
else:
    for i in range(2,int(sq+1)):
        if n%i==0:
            c+=1
            break
    if c==0:
        print("prime")
    else:
        print("composite")
    