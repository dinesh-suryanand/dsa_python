"""find the first and last position of target  in arr . if target cannot be found return [-1,-1]
    https://www.youtube.com/watch?v=Peq4GCPNC5c&t=317s

    input:
    arr = [2,4,5,5,5,5,7,9,9]
    target = 5

    output:
    [2,6]
"""


arr = [2,4,5,5,5,5,5,7,9,9]
target = 5

def brute_force(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]
    return [-1,-1]



#optiminzed solution
def find_start(arr,target):
    if arr[0] == target:
        return 0

    start , end = 0 , len(arr)-1
    

    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target and arr[mid -1] < target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

def find_end(arr, target):
    if arr[-1] == target:
        return len(arr) - 1

    start , end = 0, len(arr) - 1
    while start <= end:
        mid = (start+end) // 2

        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1

def find_first_and_last(arr,target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1,-1]
    
    start = find_start(arr,target)
    end = find_end(arr,target)
    return [start ,end ]

# print(find_first_and_last(arr,target))
print(brute_force(arr,target))
print(find_first_and_last(arr,target))