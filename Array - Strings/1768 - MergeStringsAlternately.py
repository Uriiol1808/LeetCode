"""
1768. Merge Strings Alternately.

You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. 

If a string is longer than the other, append the additional letters 
onto the end of the merged string.

Return the merged string.
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ''
        if (len(word1) >= len(word2)):
            remain = word1[len(word2):]
            for i, char1 in enumerate(word1[:len(word2)]):
                output = output + char1 + word2[i]
            output = output + remain
        else:
            remain = word2[len(word1):]
            for i, char2 in enumerate(word2[:len(word1)]):
                output = output + word1[i] + char2
            output = output + remain

        return output
    
s = Solution()

# Case 1
result1 = s.mergeAlternately(word1='abc', word2='pqr')
expected1 = "apbqcr"
print(f"Result: {result1}, Expected: {expected1}")
assert result1 == expected1

# Case 2
result2 = s.mergeAlternately(word1='ab', word2='pqrs')
expected2 = "apbqrs"
print(f"Result: {result2}, Expected: {expected2}")
assert result2 == expected2

# Case 3
result3 = s.mergeAlternately(word1='abcd', word2='pq')
expected3 = "apbqcd"
print(f"Result: {result3}, Expected: {expected3}")
assert result3 == expected3