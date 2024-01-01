"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked 
is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible 
results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1

        return -1
        
        
s = Solution()

# Case 1
result1 = s.guessNumber(10)
expected1 = 6
print(f"Result: {result1}, Expected: {expected1}")
assert result1 == expected1

# Case 2
result2 = s.guessNumber(1)
expected2 = 1
print(f"Result: {result2}, Expected: {expected2}")
assert result2 == expected2

# Case 1
result3 = s.guessNumber(2)
expected3 = 1
print(f"Result: {result3}, Expected: {expected3}")
assert result3 == expected3
