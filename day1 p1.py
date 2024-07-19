# n=int(input("enter the number\n"))
xh=int(input("enter the number\n"))
xw=int(input("enter the number\n"))
xbf=int(input("enter the number\n"))
x=0
if xh==140 and xw%2==0:
    x+=1
yh=int(input("enter the number\n"))
yw=int(input("enter the number\n"))
ybf=int(input("enter the number\n"))
y=0
if (yh<=140 or yh>=118) and yw%7==0:
    y+=1
if x==1 and y==1:
    print("they will meet")
else:
    print("they will not meet")
    





