# arr=list(map(int,input().split(" ")))
# for i in range(1,len(arr)-1):
#     if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#         print(arr[i],end=" ")


# arr=list(map(int,input().split(" ")))
# count=0
# for i in range(1,len(arr)-1):
#     if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#         count=i
#         break
# print(arr[count],end=" ")


# arr=list(map(int,input().split(" ")))
# count=0
# for i in range(1,len(arr)-1):
#     if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#         count=i
#         print(arr[count],end=" ")


arr=list(map(int,input().split(" ")))
count=0
for i in range(1,len(arr)-1):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        count=i
        print(arr[count],end=" ")
if (arr[-1]>count and arr[-1]>arr[-2]):
    count=len(arr)-1
print(arr[count],end=" ")


