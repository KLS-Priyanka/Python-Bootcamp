n= int(input("enter the number"))
m= int(input("enter the number"))
s=0
p=0
for i in range(1,n+1):
    if n%i==0:
        s+=i
for i in range(1,m+1):
    if m%i==0:
        p+=i
if s//n==p//m:
    print("friendly")  
else:
    print("not friendly")

