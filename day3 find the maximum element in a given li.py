# find the maximum element in a given list
# n=list(map(int,input().split()))
# print(max(n))
n=list(map(int,input().split(" ")))
m=0
for i in range(0,len(n)):
    if n[i]>m:
        m=n[i]
print(m)

