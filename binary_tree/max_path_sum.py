'''
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from 
some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''


'''
appending nodes to a list ??

appending all the path 
summing all paths 
return max 


filed when :
    max_path_sum = 0
    because 0 > -x

changed max_path_sum = 0 to max_path_sum = -9999
    failed for [2, -1]
    because -9999 < -1 

'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    max_path_sum = -9999 

    def PathSum(self, root):

        if root == None:
            return 0

        else:
            # path_sum = root.val + path_sum

            left_sum = self.PathSum(root.left)
            right_sum = self.PathSum(root.right)

            if left_sum + right_sum + root.val > self.max_path_sum :
                self.max_path_sum = left_sum + right_sum + root.val

            return max(left_sum + root.val, right_sum + root.val)

    def maxPathSum(self, root):
        self.PathSum(root)

        if root == None:
            return 0 

        return self.max_path_sum 


root = TreeNode(2) 

root.left  = TreeNode(-1) 
# root.right = TreeNode(20)

# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

sol = Solution()
print(sol.maxPathSum(root)) 

