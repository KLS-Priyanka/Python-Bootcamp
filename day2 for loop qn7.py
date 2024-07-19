# given list of 1 to 10 numbers comma separated values print even no's
# n=list(map(int,input().split(",")))
# for i in range(1,len(n)):
#     if i%2==0:
#         print(i,end=" ")
# count even numbers in list
# n=list(map(int,input().split(",")))
# c=0
# for i in range(1,len(n)+1):
#     if i%2==0:
#         c+=1
# print(c,end=" ")
# you are given with a space separated integer list find no.of even and odd elements
n=list(map(int,input().split(" ")))
e=0
o=0
for i in n:
    if i%2==0:
        e+=1
    else:
        o+=1
print(e,o)
