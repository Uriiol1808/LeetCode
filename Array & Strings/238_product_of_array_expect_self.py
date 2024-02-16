"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums 
except nums[i].

The product of any prefix or suffix of nums is guaranteed to 
fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without 
using the division operation.
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = nums[n-1]
        for i in range(n-2, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output

s = Solution()

# Case 1
output = s.productExceptSelf(nums=[1,2,3,4])
expected = [24,12,8,6]
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 1
output = s.productExceptSelf(nums=[-1,1,0,-3,3])
expected = [0,0,9,0,0]
print(f"Result: {output}, Expected: {expected}")
assert output == expected
