"""
2300. Successful Pairs of Spells and Potions

You are given two positive integer arrays spells and potions, of length n and m 
respectively, where spells[i] represents the strength of the ith spell and potions[j] 
represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful 
if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that 
will form a successful pair with the ith spell.
"""
class Solution(object):
    def successfulPairsFirstApproach(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        pairs = [0] * len(spells)

        for spell in range(len(spells)):
            for potion in range(len(potions)):
                if spells[spell] * potions[potion] >= success:
                    pairs[spell] += 1

        return pairs
    
    def binarySearch(self, spell, spells, potions, success):
        """
        :type potions: List[int]
        :type target: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(potions) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2

            if potions[mid] * spells[spell] >= success:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return index
    
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        m = len(potions)
        pairs = [0] * n

        potions.sort()

        for spell in range(n):
            success_index = self.binarySearch(spell, spells, potions, success)
            pairs[spell] = m - success_index if success_index != -1 else 0

        return pairs
        
s = Solution()

# Case 1
output = s.successfulPairs(spells=[5,1,3], potions=[1,2,3,4,5], success=7)
expected = [4,0,3]
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 1
output = s.successfulPairs(spells=[3,1,2], potions=[8,5,8], success=16)
expected = [2,0,2]
print(f"Result: {output}, Expected: {expected}")
assert output == expected