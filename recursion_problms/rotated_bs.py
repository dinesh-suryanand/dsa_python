arr = [5,7,9,14,1,3,4] #rotatd sorted array
key = 3

def search(arr,key,s ,e):
    m =int( s + (e-s)/2)
    if s > e:
        return -1
    if arr[m] == key:
        return m
    if arr[s] < arr[m]:
        if(key >= arr[s] and key<=arr[m]):
            return search(arr,key, s, m-1)
        else:
            return search(arr,key,m+1,e)
    if key > arr[m] and key :
        return search(arr,key,m+1,e)
    return search(arr,key, s, m-1)


print(search(arr,3,0,len(arr)))