"""
1657. Determine if Two Strings are Close

Two strings are considered close if you can attain one from the other using the 
following operations:

- Operation 1: Swap any two existing characters.
For example, abcde -> aecdb

- Operation 2: Transform every occurrence of one existing character into another 
existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, 
and false otherwise.
"""

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # Basic case when words are of different length
        if len(word1) != len(word2):
            return False
        
        count_map1 = {}
        count_map2 = {}

        for letter in word1:
            if letter in count_map1:
                count_map1[letter] += 1
            else:
                count_map1[letter] = 1
        
        for letter in word2:
            if letter in count_map2:
                count_map2[letter] += 1
            else:
                count_map2[letter] = 1

        # Sets of keys are the same in both count maps
        if set(count_map1.keys()) != set(count_map2.keys()):
            return False
        
        freq1 = sorted(count_map1.values())
        freq2 = sorted(count_map2.values())
        
        return freq1 == freq2

s = Solution()

# Case 1
result1 = s.closeStrings(word1='abc', word2='bca')
expected1 = True
print(f"Result: {result1}, Expected: {expected1}")
assert result1 == expected1

# Case 2
result2 = s.closeStrings(word1='a', word2='aa')
expected2 = False
print(f"Result: {result2}, Expected: {expected2}")
assert result2 == expected2

# Case 3
result3 = s.closeStrings(word1='cabbba', word2='abbccc')
expected3 = True
print(f"Result: {result3}, Expected: {expected3}")
assert result3 == expected3

# Case 4
result4 = s.closeStrings(word1='aaabbbbccddeeeeefffff', word2='aaaaabbcccdddeeeeffff')
expected4 = False
print(f"Result: {result4}, Expected: {expected4}")
assert result4 == expected4
