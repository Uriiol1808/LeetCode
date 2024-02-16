"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant 
extra space.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums), 2):
            if i == len(sorted_nums) - 1 or sorted_nums[i] != sorted_nums[i + 1]:
                return sorted_nums[i]
    
s = Solution()

# Case 1
output = s.singleNumber(nums=[2,2,1])
expected = 1
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.singleNumber(nums=[4,1,2,1,2])
expected = 4
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 3
output = s.singleNumber(nums=[1])
expected = 1
print(f"Result: {output}, Expected: {expected}")
# assert output == expected