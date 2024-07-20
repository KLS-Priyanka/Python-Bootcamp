# replace the elements in an array with an avg of max and min element
n=list(map(int,input().split(" ")))
min=n[0]
max=n[0]
avg=0
for i in range(0,len(n)):
    if n[i]<min:
        min=n[i]
for i in range(0,len(n)):
    if n[i]>max:
        max=n[i]
avg=(max+min)//2
for i in range(0,len(n)):
    n[i]=avg
print(n)