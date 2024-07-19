# n=list(map(int,input().split(" ")))
# for i in range(0,len(n),2):
#     print(n[i],end=" ")
# you r given with a comma separated natural numbers 1 to 10 print only even numbers
n=list(map(int,input().split(",")))
for i in range(1,len(n)):
    if i%2==0:
        print(i,end=" ")