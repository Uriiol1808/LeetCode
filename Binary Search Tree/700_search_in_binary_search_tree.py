"""
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the 
subtree rooted with that node. If such a node does not exist, return null.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def treeNodeToList(self, root):
        output = []
        if root:
            output.append(root.val)
            output += self.treeNodeToList(root.left)
            output += self.treeNodeToList(root.right)
        return output

        
s = Solution()

# EXAMPLE 1

#       4
#     /  \
#    2    7
#   / \
#  1   3 
bst_root = TreeNode(4)
bst_root.left = TreeNode(2, TreeNode(1), TreeNode(3))
bst_root.right = TreeNode(7)

# Case 1
result_node = s.searchBST(bst_root, 2)
result_list = s.treeNodeToList(result_node)
expected = [2, 1, 3]
print(f"Result: {result_list}, Expected: {expected}")
assert result_list == expected

# Case 2
result_nod2 = s.searchBST(bst_root, 5)
result_lis2 = s.treeNodeToList(result_nod2)
expected2 = []
print(f"Result: {result_lis2}, Expected: {expected2}")
assert result_lis2 == expected2

# EXAMPLE 2

#       4
#     /  \
#    2    7
#   / \  / \
#  1  3  6  9
bst_root = TreeNode(4)
bst_root.left = TreeNode(2, TreeNode(1), TreeNode(3))
bst_root.right = TreeNode(7, TreeNode(6), TreeNode(9))

# Case 1
result_node = s.searchBST(bst_root, 7)
result_list = s.treeNodeToList(result_node)
expected = [7, 6, 9]
print(f"Result: {result_list}, Expected: {expected}")
assert result_list == expected

# Case 2
result_nod2 = s.searchBST(bst_root, 4)
result_lis2 = s.treeNodeToList(result_nod2)
expected2 = [4, 2, 1, 3, 7, 6, 9]
print(f"Result: {result_lis2}, Expected: {expected2}")
assert result_lis2 == expected2


