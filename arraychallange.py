"""
[1,2,3,5,6] 

[1-1 , 2-1 , (3-2 + 3-1) , (4-3 + 4-2 + 4-1) , ...]

"""
import time


arr = [1,2,3,4,5]
lis =[0]

st = time.time()



n = len(arr)

for i in range(1,n):
    index = i
    sum = 0
    
    while index > 0:
       to_add = arr[i] - arr[index -1]
       index -= 1
       sum = sum + to_add
    
    lis.append(sum)
    
print(lis)
    
e = time.time()



print("-----------------------------------------------")

print(e-st)