"""
198. House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have
security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each 
house, return the maximum amount of money you can rob tonight without
alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums:
            return 0
        
        if n <= 2:
            return max(nums)
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for x in range(2, n):
            dp[x] = max(dp[x-1], nums[x] + dp[x-2])

        return dp[-1]


s = Solution()

# Case 1
output = s.rob(nums=[1,2,3,1])
expected = 4
print(f"Results: {output}, Expected: {expected}")

# Case 2
output = s.rob(nums=[2,7,9,3,1])
expected = 12
print(f"Results: {output}, Expected: {expected}")

# Case 3
output = s.rob(nums=[2,1,1,2])
expected = 4
print(f"Results: {output}, Expected: {expected}")
