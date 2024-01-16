"""
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated 
by a single space.

Note that s may contain leading or trailing spaces or multiple 
spaces between two words. The returned string should only have 
a single space separating the words. Do not include any extra spaces.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split into a list of words
        words = s.split()
        # Reverse the order
        revresed_words = words[::-1]
        # Join the words from the list
        result = ' '.join(revresed_words)

        return result

s = Solution()

# Case 1
output = s.reverseWords(s="the sky is blue")
expected = "blue is sky the"
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.reverseWords(s=" hello world ")
expected = "world hello"
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 1
output = s.reverseWords(s="a good  example")
expected = "example good a"
print(f"Result: {output}, Expected: {expected}")
assert output == expected