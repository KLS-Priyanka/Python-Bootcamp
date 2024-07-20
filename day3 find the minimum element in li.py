n=list(map(int,input().split(" ")))
min=0
for i in range(0,len(n)):
    if n[i]<min:
        min=n[i]
print(min)

