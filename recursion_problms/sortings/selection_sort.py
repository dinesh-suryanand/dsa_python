

# nnums = [44,8,42,-2,54,-34,76,14,-60,-43,67]
nnums = [4,3,2,1]   

def selection(arr,r,c,max):
    if r == 0:
        return
    if c < r:
        if arr[c] > arr[max]:
            selection(arr,r,c+1,c)
        else:
            selection(arr,r,c+1,max)
    else:
        arr[r-1] , arr[max] = arr[max] ,arr[r-1]
        selection(arr,r-1,0,0)

selection(nnums,len(nnums),0,0)
print(nnums)