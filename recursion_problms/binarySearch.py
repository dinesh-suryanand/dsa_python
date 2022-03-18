"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
(leet code 704)
"""
nums = [-60, -43, -34, -2, 8, 14, 42, 44, 54, 67, 76]

class Solution:
    def __init__(self) -> None:
        print("constructer created")

    def search(self, nums, target: int) -> int:

        if nums[0] > target or nums[-1] < target:
            return -1
        start , end = 0, len(nums)-1
        while start <= end :
            mid = int((end + start)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            else :
                start = mid +1
        return -1

sol = Solution()

print(sol.search(nums,8))