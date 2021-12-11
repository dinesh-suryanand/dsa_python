
nnums = [44,8,42,-2,54,-34,76,14,-60,-43,67]
# nnums = [4,3,2,1]

def bubble(arr,r,c):
    if r == 0:
        return
    if c < r:
        if arr[c] > arr[c+1]:
            arr[c] , arr[c+1] = arr[c+1],arr[c]
        bubble(arr,r,c+1)
    else:
        bubble(arr,r-1,0)

bubble(nnums,len(nnums)-1,0)
print(nnums)


