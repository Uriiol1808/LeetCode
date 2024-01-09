"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false 
otherwise.

A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters. (i.e., "ace" is a 
subsequence of "abcde" while "aec" is not).
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ptr, t_ptr = 0, 0
        subsequence = ''

        while s_ptr < len(s) and t_ptr < len(t):
            # s str will always be smaller than t string
            if s[s_ptr] == t[t_ptr]:
                subsequence += s[s_ptr]
                s_ptr += 1
            t_ptr += 1
        
        return subsequence == s
    
s = Solution()

# Case 1
output = s.isSubsequence(s='abc', t='ahbgdc')
expected = True
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.isSubsequence(s='axc', t='ahbgdc')
expected = False
print(f"Result: {output}, Expected: {expected}")
assert output == expected