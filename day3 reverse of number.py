n=int(input())
rev=""
while n>0:
    t=n%10
    rev=rev+str(t)
    n=n//10
print(rev)