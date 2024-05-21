"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower 
and upper cases, more than once.
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s)-1 # Two pointers

        while left < right:
            while left < right and s[left].lower() not in vowels:
                left += 1
            while left < right and s[right].lower() not in vowels:
                right -= 1

            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

s = Solution()

# Case 1
output = s.reverseVowels('hello')
expected = 'holle'
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
output = s.reverseVowels('leetcode')
expected = 'leotcede'
print(f"Result: {output}, Expected: {expected}")
assert output == expected