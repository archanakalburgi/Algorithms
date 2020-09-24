'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from 
the root node down to the farthest leaf node.

Note: A leaf is a node with no children.


Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None :
            return 0 
        else :
            print(root.val)
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left,right)+1 
        

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20) 
root.right.left = TreeNode(15) 
root.right.right = TreeNode(7) 

sol = Solution()
print(sol.maxDepth(root)) 
        

