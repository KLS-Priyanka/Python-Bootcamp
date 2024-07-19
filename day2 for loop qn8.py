# given an space separated integer list find the avd of elements present in even index
l=list(map(int,input().split(" ")))
s=0
for i in l:
    if i%2==0:
        s+=i
        avg=s/len(l)
print(avg)