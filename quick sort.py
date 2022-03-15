nums = [44,8,42,-2,54,-34,76,14,-60,-43,67]

def quickSort(arr,low ,hi):
    if low > hi:
        return
    s,e = low,hi
    m = s+(e-s)/2
    p = arr[m]
    while s<=e:
        while nums[s] < p:
            s += 1
        while nums[e] > p:
            e -= 1
        if s <= e:
            nums[e] , nums[s] = nums[s], nums[e]
            s += 1
            e -= 1
        quickSort(arr,low, e)
        quickSort(arr,s,hi)

print(quickSort(nums,0,len(nums)-1))