# print the element in the particular index in cyclic order
k=int(input("enter the number"))
l=list(map(int,input().split(" ")))
a=k%len(l)
print(l[a])

