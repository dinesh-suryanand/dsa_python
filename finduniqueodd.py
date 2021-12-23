arr = [2,4,6,7,4,2,6,2,4,6]#repeated 3 times

def findUniqueOdd(arr):
    res = 0
    for i in arr:
        res = res ^ i
    return res

print(findUniqueOdd(arr))
