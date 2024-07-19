n=int(input("enter the number\n"))
temp=n
s=0
while(temp>0):
    a=temp%10
    fact=1
    for i in range(1,a+1):
        fact*=i
    s+=fact
    temp=temp//10
if (s==n):
    print(f"{n} is a strong number")
else:
    print(f"{n} is not a strong number")