nnums = [44,8,42,-2,54,-34,76,14,-60,-43,67]


def bubbleSort(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(0,l-i-1):
            if arr[j] > arr[j+1]:
                arr[j] ,arr[j+1] = arr[j+1] , arr[j]
    return arr

print(bubbleSort(nnums))