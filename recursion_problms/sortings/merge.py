nums = [44,8,42,-2,54,-34,76,14,-60,-43,67]
nums = [4,1,3,2,5]

def mergeSort(arr):
    if len(arr) ==1:
        return arr
    mid = int(len(arr)/2)
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:len(arr)])
    return merge(left,right)

def merge(first,second):
    mix = []
    i= 0
    j =0
    while i< len(first) and  j < len(second):
        if first[i] < second[j]:
            mix.append(first[i])
            i += 1
        else:
            mix.append(second[j])
            j += 1
    while i< len(first):
        mix.append(first[i])
        i +=1
    while j< len(second):
        mix.append(second[j])
        j += 1
    return mix

print(mergeSort(nums))