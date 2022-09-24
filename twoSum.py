# Solution for Two Sum question on LeetCode.

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Brute Force Solution with O(n*2) Time Complexity.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j] == target and i!=j:
                    return [i,j]
                


# Optimized using Hashmap and two Pointers with O(n) Time Complexity.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict1 = {}
        
        for idx,ele in enumerate(nums):
            diff = target-ele
            if diff in dict1:
                return [dict1[diff],idx]
            dict1[ele] = idx
            

