"""
    Linear search using recursion ,

"""

arr = [4,7,9,14,23,36,48, 48,52,68,72, 48,84,97]

key = 4

#retun true or false if number exists
def linear_search(arr,index, key):
    if index == len(arr) -1:
        return False
    return arr[index] == key or linear_search(arr,index+1,key)

print(linear_search(arr,0,key)) # returns True




key = 48
#returns a list containting the indexes of the key i.e 48
lis =[]
def linear_search_similar(arr,index, key,lis):
    if index == len(arr):
        return lis
    if arr[index] == key:
        lis.append(index)
    return linear_search_similar(arr,index+1,key,lis)

print(linear_search_similar(arr,0,key,lis)) #returns list [6, 7, 11]