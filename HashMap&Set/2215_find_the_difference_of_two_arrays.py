"""
2215. Find the Difference of Two Arrays.

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer1 = set()
        answer2 = set()

        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        for num in set_nums1:
            if num not in set_nums2:
                answer1.add(num)

        for num in set_nums2:
            if num not in set_nums1:
                answer2.add(num)

        return [list(answer1), list(answer2)]

s = Solution()

# Case 1
result1 = s.findDifference(nums1=[1,2,3], nums2=[2,4,6])
expected1 = [[1,3],[4,6]] 
print(f"Result: {result1}, Expected: {expected1}")
assert result1 == expected1

# Case 2
result2 = s.findDifference(nums1=[1,2,3,3], nums2=[1,1,2,2])
expected2 = [[3],[]] 
print(f"Result: {result2}, Expected: {expected2}")
assert result2 == expected2