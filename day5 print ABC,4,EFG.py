# print ABC,4,EFG
n=input("enter the string")
# a=n.upper()
for i in n:
    print(chr(ord(i)+4),end=" ")