def generate_sub_lists(arr):
    sub_list = [[]] 
    for i in range(len(arr) + 1):
        for j in range(i + 1, len(arr) + 1):
            sub = arr[i:j] 
            sub_list.append(sub) 
      
    return sub_list 


def maxBeauty(N, A):
    sub_lists = generate_sub_lists(A)
    max = sum(sub_lists[0])
    for i in sub_lists:
        if sum(i) > max:
            max = sum(i)
            max_sum_array = i
    ans_lis =[]
    for i in max_sum_array:
        ans_lis.append(i*max)
    ans = 0
    for ele in ans_lis:
        if ele > ans:
            ans = ele
    return ans
    

# print(maxBeauty([5,2,-5,-2]))

print('a' *2)
print(float('24.5') *2 )
