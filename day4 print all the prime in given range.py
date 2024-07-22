# write a program to print all the prime numbers in a given range
n=int(input("enter the number"))
m=int(input("enter the number"))
c=0
# sq=n**0.5
# if n==1:
#     print("neither prime nor composite")
# else:
for i in range(n,m+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
    