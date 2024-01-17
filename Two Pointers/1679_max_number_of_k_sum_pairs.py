"""
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose 
sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        operations = 0
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                operations += 1
                left += 1
                right -= 1
            # As the array is now sorted, we can do this:
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return operations

s = Solution()

# Case 1
output = s.maxOperations(nums=[1,2,3,4], k=5)
expected = 2
print(f"Results: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.maxOperations(nums=[3,1,3,4,3], k=6)
expected = 1
print(f"Results: {output}, Expected: {expected}")
assert output == expected

# Case 3
output = s.maxOperations(nums=[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], k=2)
expected = 2
print(f"Results: {output}, Expected: {expected}")
assert output == expected