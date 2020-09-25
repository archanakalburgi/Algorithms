'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
'''

# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class Solution:
    def isUnivalTree(self, root):
        """
        i/p: TreeNode
        o/p: True/False -> bool
        """
        left = root.left == None or root.left.val == root.val and self.isUnivalTree(root.left)
        right = root.right == None or root.right.val == root.val and self.isUnivalTree(root.right)
        return left and right 

         

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1) 
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1) 


sol = Solution()
print(sol.isUnivalTree(root)) 
