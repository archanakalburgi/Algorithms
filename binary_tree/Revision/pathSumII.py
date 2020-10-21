'''
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def paths(self, root, sum, nodesList, pathsList):
        if root == None:  
                return pathsList 

        else :
            
            if root.val == sum and root.left == None and root.right == None:   
                return pathsList + [nodesList + [root.val]] 

            else :
                left = self.paths(root.left, sum - root.val, nodesList + [root.val] , pathsList)  
                right = self.paths(root.right, sum - root.val, nodesList + [root.val] , pathsList) 

            return left + right 

    def pathSum(self, root, sum):  
        if root == None:
            return None
        return self.paths(root, sum, [], [])

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8) 
root.left.left = TreeNode(11)
root.left.left.right = TreeNode(2) 
root.left.left.left = TreeNode(7) 
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1) 

sol = Solution()
print(sol.pathSum(root,22)) 