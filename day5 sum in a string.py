n=input("enter the string")
s=0
for i in n:
    if i.isdigit():
        s+=int(i)
print(s)


n=input("enter the string")
s=0
for i in n:
    if i in ord('0') >= ord('9'):
        s+=i
print(s)