# find the element present in k+ith index 
k=3
a=2
b=k+a
n=list(map(int,input().split(" ")))
if len(n)<b:
    print("error")
else:
    for i in n:
        if i==b:
            break
print(i)
