nnums = [44,8,42,-2,54,-34,76,14,-60,-43,67]
nnums.sort()
print(nnums)
toFind = 76


def binarySearch(arr , taget):
    s = 0
    e = len(arr) - 1

    while s <= e :
        m = int(s + (e-s)/2)

        if arr[m] == taget:
            return m
        elif arr[m] > taget:
            e = m - 1
        else:
            s = m + 1

    return -1

print(binarySearch(nnums,toFind))