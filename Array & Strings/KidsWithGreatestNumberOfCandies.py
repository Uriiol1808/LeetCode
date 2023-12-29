"""
There are n kids with candies. You are given an integer array candies, where 
each candies[i] represents the number of candies the ith kid has, and an 
integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, 
after giving the ith kid all the extraCandies, they will have the greatest 
number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        

s = Solution()

# Case 1
result1 = s.kidsWithCandies(candies=[2,3,5,1,3], extraCandies=3)
expected1 = [True,True,True,False,True] 
print(f"Result: {result1}, Expected: {expected1}")
assert result1 == expected1

# Case 2
result2 = s.kidsWithCandies(candies=[4,2,1,1,2], extraCandies=1)
expected2 = [True,False,False,False,False]
print(f"Result: {result2}, Expected: {expected2}")
assert result2 == expected2

# Case 3
result3 = s.kidsWithCandies(candies=[12,1,12], extraCandies=10)
expected3 = [True,False,True]
print(f"Result: {result3}, Expected: {expected3}")
assert result3 == expected3