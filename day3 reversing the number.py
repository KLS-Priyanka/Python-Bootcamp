n=int(input("enter the number"))
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
print(s)   


# 2nd method
n=int(input("enter the number"))
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(rev)
print(int(rev))

