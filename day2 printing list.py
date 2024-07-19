# p=[1,2,3,4,2,2,4,4]
# p.append(7)
# print(p)
# p.insert(0,999)
# print(len(p))
# print(*p)
# c=p.count(2)
# print(c)
# p.sort()
# print(p)
# p.pop()
# print(p)
# hp=[11,12,1,3,14,15]

# p=list(map(str,input().split(",")))
# p=list(map(int,input().split(",")))
# # p.append(6)
# print(*p)
# c=p.count(2)
# print(c)
# p.sort()
# print(*p)
l=list(map(int,input().split()))
c=int(input())
if c==1:
    l.append(8)
    print(*l)
elif c==2:
    l.pop(4)
    print(*l)
elif c==3:
    l.sort()
    print(*l)

