l=list(map(int,input().split(" ")))
n=len(l)+1
s=0
m=n*(n+1)//2
print(m)
for i in l:
    s+=i
a=m-s
print(a)
