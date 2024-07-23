# wap to print all the capital letters in a string
n=input("enter the string")
for i in n:
    if (ord(i)>=65 and ord(i)<=90):
        # s+=int(i)
        print(i)