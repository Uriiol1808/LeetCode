"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 
will be accepted.
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
s = Solution()

# Case 1
output = s.findMaxAverage(nums=[1,12,-5,-6,50,3], k=4)
expected = 12.75000
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.findMaxAverage(nums=[5], k=1)
expected = 5.0000
print(f"Result: {output}, Expected: {expected}")
assert output == expected
