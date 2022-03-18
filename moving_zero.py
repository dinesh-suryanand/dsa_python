lis = [0,0,1,2,3,0,-1,0,7]

# for i in range(len(lis)):
#     if lis[i] == 0:
#         continue
#     else:
#         lis[i], lis[j] = lis[j], lis[i]
#         j +=1

# print(lis)
j=0
for i in lis:
    if i == 0:
        continue
    else:
        i , lis[j] = lis[j] , i
        j+=1

print(lis)
