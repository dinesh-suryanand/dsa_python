arr = [4,7,9,14,23,36,48,52,68,72,84,97]

def sort_or_not(arr,index):
    if index == len(arr) -1:
        return True
    return arr[index] < arr[index +1] and sort_or_not(arr , index+1)

print(sort_or_not(arr,0))