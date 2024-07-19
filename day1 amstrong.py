n=int(input("enter the number\n"))
h=list(str(n))
s=0
for i in h:
    a=int(i)**len(h)
    s+=a
if s==n:
    print(f"{n} is an amstrong number")
else:
    print(f"{n} is not an amstrong number")
