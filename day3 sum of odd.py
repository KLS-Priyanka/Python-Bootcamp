n=int(input())
s=0
while n>0:
    t=n%10
    if t%2!=0:
        s+=t
    n=n//10
print(s)