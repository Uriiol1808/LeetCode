"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, 
the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is 
(6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value 
sequence is the same.

Return true if and only if the two given trees with head nodes root1 
and root2 are leaf-similar.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leaf_sequence(node, leaves):
            if node is not None:
                if node.left is None and node.right is None:
                    leaves.append(node.val)
                leaf_sequence(node.left, leaves)
                leaf_sequence(node.right, leaves)
            
        leaves1, leaves2 = [], []
        leaf_sequence(root1, leaves1)
        leaf_sequence(root2, leaves2)

        return leaves1 == leaves2
        
s = Solution()

# EXAMPLE 1

#            3               3
#          /   \           /   \
#         5     1         5     1
#        / \   / \       / \   / \
#       6   2 9   8     6   7  4  2
#          / \                   / \
#         7   4                 9   8 
bst_root1 = TreeNode(3)
bst_root1.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
bst_root1.right = TreeNode(1, TreeNode(9), TreeNode(8))

bst_root2 = TreeNode(3)
bst_root2.left = TreeNode(5, TreeNode(6), TreeNode(7))
bst_root2.right = TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8)))

output = s.leafSimilar(bst_root1, bst_root2)
expected = True
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# EXAMPLE 2

#     1      1
#    / \    / \
#   2   3  3   2
bst_root1 = TreeNode(1, TreeNode(2), TreeNode(3))
bst_root2 = TreeNode(1, TreeNode(3), TreeNode(2))

output = s.leafSimilar(bst_root1, bst_root2)
expected = False
print(f"Result: {output}, Expected: {expected}")
assert output == expected

