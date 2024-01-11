"""
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on 
a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        
        # Base cases
        first = cost[0]
        second = cost[1]
        if (n <= 2):
            return min(first, second)
        
        for i in range(2, n):
            curr = cost[i] + min(first, second)
            first = second
            second = curr
        
        return min(first, second)
        

s = Solution()

# Case 1
output = s.minCostClimbingStairs(cost=[10, 15, 20])
expected = 15
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.minCostClimbingStairs(cost=[1,100,1,1,1,100,1,1,100,1])
expected = 6
print(f"Result: {output}, Expected: {expected}")
assert output == expected