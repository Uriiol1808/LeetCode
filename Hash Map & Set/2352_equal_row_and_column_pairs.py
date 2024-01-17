"""
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the 
same order (i.e., an equal array).
"""

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pairs = 0
        for col in range(len(grid)):
            column = []
            for row in grid:
                column.append(row[col]) # Transform row into column
            pairs += grid.count(column)
        
        return pairs

s = Solution()

# Case 1

# | 3 | 2 | 1 |
# | 1 | 7 | 6 |
# | 2 | 7 | 7 |

output = s.equalPairs(grid=[[3,2,1],[1,7,6],[2,7,7]])
expected = 1
print(f"Result: {output}, Expected: {expected}")
# assert output == expected

# {row1: 1, row2: 0, row3: 0} --> 1
# Case 2

# | 3 | 1 | 2 | 2 |
# | 1 | 4 | 4 | 5 |
# | 2 | 4 | 2 | 2 |
# | 2 | 4 | 2 | 2 |

output = s.equalPairs(grid=[[3,1,2,2],[1,4,4,5],
                            [2,4,2,2],[2,4,2,2]])
expected = 3
print(f"Result: {output}, Expected: {expected}")
# assert output == expected

# {row1: 1, row2: 0, row3: 1, row4: 1} --> 1