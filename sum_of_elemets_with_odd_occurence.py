
arr = list(map(int,input().split()))
arr = arr.sort()
cc={}

arr.sort()


def count_fun(n):
    count = 0
    for i in range(1,len(arr)):
        if(arr[i] == arr[i-1]):
            count += 1
    cc[n] = count

set_array = set(arr)
set_array = list(set_array)
for i in set_array:
    count_fun(i)


print(cc)




# alternate soln
# arr=list(map(int,input().split()))
# s=set(arr)
# s=list(s)
# res={}


# def coun(j):
#     cc=0
#     for i in arr:
#         if i == j:
#             cc+=1
#     return cc
# for i in s:
#     x=coun(i)
#     res[i]=x
# print(res)
# sum=0
# for i in res:
#     if int(res[i])%2 != 0:
#         sum=sum+i
# print(sum)