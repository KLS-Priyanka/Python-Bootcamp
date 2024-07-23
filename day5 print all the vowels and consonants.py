# print all the vowels and consonants
# n=input("enter the string")
# m=['a','e','i','o','u']
# cons="bcdfghjklmnpqrstvwxyz"
# b=n.lower()
# for i in m:
#     if i in b:
#         print(i,end=" ")
# print()
# for i in b:
#     if i in cons:
#         print(i,end=" ")


n=input("enter the string")
m=['a','e','i','o','u']
cons="bcdfghjklmnpqrstvwxyz"
b=n.lower()
ans=""
for i in m:
    if i in b:
        ans+=i
for i in b:
    if i in cons:
        ans+=i
print(ans)