'''
226. Invert Binary Tree


Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        if root == None:
            return None

        else :
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            root.left = right 
            root.right = left 

            return root 

root = TreeNode(4)
root.left = TreeNode(7)
root.right = TreeNode(2)
root.left.left = TreeNode(9)
root.left.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(1)

sol =  Solution()
print(sol.invertTree(root))