# hell0----wor--ld
n=input("enter the string")
str=""
c=0
for i in n:
    if i=='-':
        c+=1
    else:
        str+=i
print("-"*c,str)