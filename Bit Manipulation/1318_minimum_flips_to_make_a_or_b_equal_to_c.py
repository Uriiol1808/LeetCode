"""
1318. Minimum Flips to Make a OR b Equal to c

Given 3 positives numbers a, b and c. Return the minimum flips required in some 
bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 
in their binary representation.
"""

class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0

        # Integers are 32-bit
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1

            # Check if bitwise OR operation is not equal to c
            if (bit_a | bit_b) != bit_c:
                flips += (bit_a + bit_b) if bit_c == 0 else 1

        return flips
        
s = Solution()

# Case 1
output = s.minFlips(a=2, b=6, c=5)
expected = 3
print(f"Result: {output}, Expected: {expected}")
# assert output == expected

# Case 2
output = s.minFlips(a=4, b=2, c=7)
expected = 1
print(f"Result: {output}, Expected: {expected}")
# assert output == expected

# Case 3
output = s.minFlips(a=1, b=2, c=3)
expected = 0
print(f"Result: {output}, Expected: {expected}")
# assert output == expected