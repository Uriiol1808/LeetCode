"""
443. String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

- If the group's length is 1, append the character to s.

- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths that 
are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        string = ''
        for letter in chars:
            if letter not in string:
                string += letter + \
                (str(chars.count(letter)) if chars.count(letter) > 1 else "")

        return list(string)
    # not finished

s = Solution()

# Case 1
output = s.compress(chars=["a","a","b","b","c","c","c"])
# expected = ["a","2","b","2","c","3"]
expected = 6
print(f"Result: {output}, Expected: {expected}")

# Case 2
output = s.compress(chars=["a"])
# expected = ["a"]
expected = 1
print(f"Result: {output}, Expected: {expected}")

# Case 3
output = s.compress(chars=["a","b","b","b","b","b","b","b","b","b","b","b","b"])
# expected = ["a","b","1","2"]
expected = 4
print(f"Result: {output}, Expected: {expected}")
