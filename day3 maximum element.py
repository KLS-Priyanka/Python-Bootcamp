arr=list(map(int,input().split(" ")))
m=arr[0]
for i in range (len(arr)):
    if arr[i]>m:
        m=arr[i]
print(m)