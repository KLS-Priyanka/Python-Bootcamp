# reverse the number in a given string
n=input("enter the string")
m="0123456789"
s=""
for i in n:
    if i in m:
        s+=i
print(s)
s1=int(s)
s2=""
while(s1>0):
     rem=s1%10
     s2+=str(rem)
     s1=s1//10
print(s2)
