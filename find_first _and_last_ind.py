"""
    to find the first and last  index in an element in a sorted array 
    
    input:[1,2,5,7,7,7,7,9,13,13] target = 7
    output:[3,6]
    
    input:[1,2,5,7,7,7,7,9,13,13] target = 3
    output:[-1,-1]
"""

from turtle import right


arr = [1,2,5,7,7,7,7,9,13,13]
target =13

def indexs(arr, target):
    left = updatedBS(arr,target,True)
    right = updatedBS(arr,target,False)
    return [left,right]
    
def updatedBS(arr,target , isLeftBiased):
    l ,r = 0 ,len(arr) - 1
    i = -1 
    while l <= r:
        mid = (l+r)//2
            
        if arr[mid] > target: 
            r = mid - 1
        elif arr[mid] < target:
            l = mid +1
        else:
            i = mid
            if isLeftBiased:
                
                r = mid - 1
            else:
                l = mid + 1
    return i

print(indexs(arr,target))

