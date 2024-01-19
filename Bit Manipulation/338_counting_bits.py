"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.
"""

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        bitCountArray = []
        for i in range(0, n + 1):
            bitCount = bin(i)[2:].count('1')
            bitCountArray.append(bitCount)
        
        return bitCountArray

s = Solution()

# Case 1
output = s.countBits(n=2)
expected = [0,1,1]
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.countBits(n=5)
expected = [0,1,1,2,1,2]
print(f"Result: {output}, Expected: {expected}")
assert output == expected
