"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining
 the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1

        return nums

s = Solution()

# Case 1
result1 = s.moveZeroes(nums=[0,1,0,3,12])
expected1 = [1,3,12,0,0]
print(f"Result: {result1}, Expected: {expected1}")
assert result1 == expected1

# Case 2
result2 = s.moveZeroes(nums=[0])
expected2 = [0]
print(f"Result: {result2}, Expected: {expected2}")
assert result2 == expected2