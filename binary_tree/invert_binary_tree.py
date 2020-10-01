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

'''
    1           mirror image 
   / \
  2   3

    1
   / \
  3   2

1. construch new binary tree from nodes ???
post -> 2,3,1
pre -> 1,2,3 

- swap left and right 
temp = left
left = right 
right = temp 

- repeat the above for ull tree ??


'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
