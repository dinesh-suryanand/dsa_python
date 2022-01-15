"""
Kth largest element problem you have given an array of integers , and integer k
find the kth larget element

input:
arr = [4,2,5,7,9,6,7,1,3]
k = 4

output:
6

https://www.youtube.com/watch?v=Peq4GCPNC5c&t=827s
"""


#remove the maimum element upto k times then the remaining maximum element is the ans

arr = [4,2,5,7,9,6,7,1,3]
k = 4

def brute_force(arr,k):                 # time complexity O(kn) idi bokka 
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

#sorting the arr
def sorting_solution(arr,k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

#optimum solution is using priority queue ---> priority queue is often implementd by heap
import heapq 


def kth_largest(arr,k):
    arr = [-ele for ele in arr]                 #in python we have min heap , to convet into max heap we muliply with -1
    
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    
    return -heapq.heappop(arr)                  #since we muliply with -1 we are returing the nevitive value of it

print(kth_largest(arr,k))