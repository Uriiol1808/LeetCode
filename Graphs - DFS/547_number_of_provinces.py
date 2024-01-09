"""
547. Number of Provinces.

There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected 
directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and 
no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 
if the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        provinces = 0
        
s = Solution()

# Case 1
# 1 1 0
# 1 1 0
# 0 0 1
result = s.findCircleNum(isConnected=[[1,1,0],[1,1,0],[0,0,1]])
expected = 2
print(f"Result: {result}, Expected: {expected}")
assert result == expected

# Case 2
# 1 0 0
# 0 1 0
# 0 0 1
result = s.findCircleNum(isConnected=[[1,0,0],[0,1,0],[0,0,1]])
expected = 3
print(f"Result: {result}, Expected: {expected}")
assert result == expected