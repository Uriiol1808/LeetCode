"""
605. Can Place Flowers.

You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means
empty and 1 means not empty, and an integer n, return true if n new flowers 
can be planted in the flowerbed without violating the no-adjacent-flowers
rule and false otherwise.
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        planted = 0
        i = 0

        while i < len(flowerbed):
            # If there is not a flower
            if flowerbed[i] == 0:
                # Check adjacent positions
                prev_empty = (i == 0 or flowerbed[i-1] == 0)
                next_empty = (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)

                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    planted += 1
                    i += 2
                    continue
            
            # Next empty spot
            i += 1

        return planted >= n

s = Solution()

# Case 1
output = s.canPlaceFlowers(flowerbed=[1,0,0,0,1], n=1)
expected = True
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.canPlaceFlowers(flowerbed=[1,0,0,0,1], n=2)
expected = False
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 3
output = s.canPlaceFlowers(flowerbed=[1,0,0,0,0,0,1], n=2)
expected = True
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 4
output = s.canPlaceFlowers(flowerbed=[0,1,0,1,0,1,0,0], n=1)
expected = True
print(f"Result: {output}, Expected: {expected}")
assert output == expected

        