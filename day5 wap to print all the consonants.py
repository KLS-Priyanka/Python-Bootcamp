# wap to print all the consonants
n=input("enter the string")
m=['a','e','i','o','u']
cons="bcdfghjklmnpqrstvwxyz"
c=0
count=0
b=n.lower()
for i in m:
    if i in b:
        c+=1
for i in b:
    if i in cons:
        count+=1
print(c,count)