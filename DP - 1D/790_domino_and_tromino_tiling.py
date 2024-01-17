"""
790. Domino and Tromino Tiling

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. 
You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. 
Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are 
different if and only if there are two 4-directionally adjacent cells 
on the board such that exactly one of the tilings has both squares 
occupied by a tile.
"""

class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        

s = Solution()

# Case 1
output = s.numTilings(n=3)
expected = 5
print(f"Result: {output}, Expected: {expected}")

# Case 2
output = s.numTilings(n=1)
expected = 1
print(f"Result: {output}, Expected: {expected}")