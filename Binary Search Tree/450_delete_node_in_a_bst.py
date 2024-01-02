"""
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node 
with the given key in the BST. Return the root node reference 
(possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        # Find node to remove
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 2: Node with two children (take the smallest)
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root
      
    def findMin(self, node):
        # Find the leftmost node
        while node.left:
            node = node.left
        return node
    
    def inorderTraversal(self, root):
        output = []
        if root:
            output.append(root.val)
            output += self.inorderTraversal(root.left)
            output += self.inorderTraversal(root.right)
        return output
    
s = Solution()

# EXAMPLE 1

#       5                   5
#     /  \     key = 3     / \
#    3    6     ---->     4   6
#   / \    \             /     \
#  2   4    7           2       7

# Another valid answer is:
#       5                   5
#     /  \     key = 3     / \
#    3    6     ---->     2   6
#   / \    \               \   \
#  2   4    7               4   7

bst_root = TreeNode(5)
bst_root.left = TreeNode(3, TreeNode(2), TreeNode(4))
bst_root.right = TreeNode(6, right=TreeNode(7))

# Case 1
new_root = s.deleteNode(bst_root, 3)
resulting_bst = s.inorderTraversal(new_root)
expected = [5, 4, 6, 2, None, None, 7]
print(f"Result: {resulting_bst}, Expected: {expected}")
