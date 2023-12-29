"""
1207. Unique Number of Occurrrences.

Given an array of integers arr, return true if the number of occurrences
of each value in the array is unique or false otherwise.
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count_map = {}

        # Count occurrences
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        occurrence_set = set(count_map.values())
        return len(occurrence_set) == len(count_map)

s = Solution()

# Case 1
result1 = s.uniqueOccurrences(arr=[1,2,2,1,1,3])
expected1 = True
print(f"Result: {result1}, Expected: {expected1}")
assert result1 == expected1

# Case 2
result2 = s.uniqueOccurrences(arr=[1,2])
expected2 = False
print(f"Result: {result2}, Expected: {expected2}")
assert result2 == expected2

# Case 3
result3 = s.uniqueOccurrences(arr=[-3,0,1,-3,1,1,1,-3,10,0])
expected3 = True
print(f"Result: {result3}, Expected: {expected3}")
assert result3 == expected3