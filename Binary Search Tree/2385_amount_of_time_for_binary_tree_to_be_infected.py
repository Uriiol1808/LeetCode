"""
2385. Amount of Time for Binary Tree to Be Infected.

You are given the root of a binary tree with unique values, 
and an integer start. At minute 0, an infection starts 
from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire 
tree to be infected.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        def dfs(node, current_minutes):
            nonlocal max_minutes
            
            if node.val == start:
                current_minutes = 0

            if node.left and node.left.val not in infected_nodes:
                infected_nodes.add(node.left.val)
                dfs(node.left, current_minutes+1)
            if node.right and node.right not in infected_nodes:
                infected_nodes.add(node.right.val)
                dfs(node.right, current_minutes + 1)
                
            max_minutes = max(max_minutes, current_minutes)

        if not root:
            return 0
        
        infected_nodes = {start}
        max_minutes = 0

        dfs(root, 0)

        return max_minutes


s = Solution()

# EXAMPLE 1
#            1 
#          /    \
#         5      3
#          \    / \
#           4  10  6
#          / \
#         9   2

bst_root = TreeNode(1)
bst_root.left = TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2)))
bst_root.right = TreeNode(3, TreeNode(10), TreeNode(6))

output = s.amountOfTime(root=bst_root, start=3)
expected = 4
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# EXAMPLE 2
#        1
bst_root = TreeNode(1)

output = s.amountOfTime(root=bst_root, start=1)
expected = 0
print(f"Result: {output}, Expected: {expected}")
assert output == expected