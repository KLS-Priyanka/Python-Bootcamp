# check how many vowels are in a string
n=input("enter the string")
m=['a','e','i','o','u']
c=0
for i in m:
    if i in n:
        c+=1
print(c)