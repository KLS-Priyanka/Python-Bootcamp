# gcd of 2 numbers
a=int(input("enter the number"))
b=int(input("enter the number"))
while b!=0:
     a,b=b,a%b
print("gcd of 2 numbers is :",a)