# print the non repeating characters in a string
n=input("enter the string")
m=""
for i in n:
    if i not in m:
        m+=i
print(m)