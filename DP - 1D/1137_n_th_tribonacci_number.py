"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return s.tribonacci(n - 1) + s.tribonacci(n - 2) + s.tribonacci(n - 3)
        

s = Solution()

# Case 1
output = s.tribonacci(4)
expected = 4
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.tribonacci(25)
expected = 1389537
print(f"Result: {output}, Expected: {expected}")
assert output == expected