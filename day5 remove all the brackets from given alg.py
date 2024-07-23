# remove all the brackets from given algebraic expression
n=input("enter the string")
str=""
for i in n:
    if ord(i)!=91 and ord(i)!=93 and ord(i)!=123 and ord(i)!=125 and ord(i)!=40 and ord(i)!=41:
        str+=i
print(str)


n=input("enter the string")
for i in n:
    if ord(i)!=91 or ord(i)!=93 or ord(i)!=123 or ord(i)!=125 or ord(i)!=40 or ord(i)!=41:
        pass
    else:
        print(i,end="")
print()