'''
250. Count Univalue Subtrees

Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Example 1: 

Input: root = [5,1,5,5,5,null,5]
Output: 4


Example 2:

Input: root = []
Output: 0


Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    count = 0 
    def countNodes(slef, root):
        if root == None :
            return True 
        
        left = self.countNodes(root.left, count) 
        right = self.countNodes(root.right, count) 

        if left == False or right == False:
            return False

        if root.left and root.val != root.left.val:
            return False 

        if root.right and root.val != root.left.val:
            return False
        
        self.count = self.count + 1
        return True

    def countUnivalSubtrees(self, root, count = 0):
        if root == None:
            return 0
        return self.count 

root = TreeNode(5)
root.left = TreeNode(1) 
root.right = TreeNode(5)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
root.right.right = TreeNode(5)

sol = Solution()
print(sol.countUnivalSubtrees(root))  