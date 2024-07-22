# leap year
# n=int(input("enter the number"))
# m=int(input("enter the number"))
# for i in range(n,m+1):
#     if i%4==0 or i%400==0 and i%100!=0:
#         print(i)


n=int(input("enter the number"))
if n%4==0 or n%400==0 and n%100!=0:
    print("leap year")
else:
    print("not leap year")