'''
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that 
adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def path(self, root, sum):
        if root == None:
            return False 
         
        if root.left == None and root.right == None and sum - root.val == 0 :
            return True

        return self.path(root.left, sum-root.val) or self.path(root.right, sum-root.val) 
    
    def hasPathSum(self, root, sum):

        if root == None :
            return 
        
        else :
            return self.path(root, sum) 

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8) 
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13) 
root.right.right = TreeNode(4) 
root.right.right.right =  TreeNode(1)

sol = Solution()
print(sol.hasPathSum(root, 22))



'''
path can be either on right or left or mix 

return False as base case : because if reached the leaf and yet not found required path return False is base case 

keep decrementing the given sum by every node val till sum is exhaused 

why not bottom to top ?
    problem requirement - has to come from root to leave in order to collect the nodes and check for the requried path 
'''