n=int(input())
rev=""
o_n=n
while n>0:
    t=n%10
    rev=rev+str(t)
    n=n//10
if rev==str(o_n):
    print("n is palindrome")   
else:
    print("n is not palindrome")