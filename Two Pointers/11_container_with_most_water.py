"""
11. Container With Most Water

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            h = min(height[left_pointer], height[right_pointer])
            w = right_pointer - left_pointer
            max_water = max(max_water, h * w)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water

s = Solution()

# Case 1
#   |              |
#   |              |     |
#   |  |           |     |
#   |  |     |     |     |
#   |  |     |  |  |     |
#   |  |     |  |  |  |  |
#   |  |  |  |  |  |  |  |
# | |  |  |  |  |  |  |  |
result = s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
expected = 49
print(f"Result: {result}, Expected: {expected}")
assert result == expected

# Case 2
result2 = s.maxArea(height=[1, 1])
expected2 = 1
print(f"Result: {result2}, Expected: {expected2}")
assert result2 == expected2
