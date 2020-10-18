'''
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree 
along the parent-child connections. The path must contain at least one node and does not need to go through the root.


Example 1:
            1
          /   \
         2     3

Input: root = [1,2,3]
Output: 6

Example 2:

        -10
      /      \
    9         20
            /     \
           15       7

Input: root = [-10,9,20,null,null,15,7]
Output: 42

'''

'''
max sum can be in the left subtree
max sum can be in the right sub tree 
max sum can be left+right+root 


'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    maxSum = -999

    def helper(self, root): 
        # if root == None or root.val < 0:  # won't work because a tree could have a -ve root, wont left further execution 
        #     return 0 

        if root == None:
            return 0 
        
        maxLeftSum = self.helper(root.left)
        maxRightSum = self.helper(root.right)

        # if maxLeftSum <= 0:   # it is necessary in order to deal with negetive root values 
        #     maxLeftSum = 0      # if maxLeftSum = -10 , -10 > -999 , so maxSum become -10 
        #                         # when a leaf is -vie we need 0 to be returned 
        # if maxRightSum <=0:
        #     maxRightSum = 0 

        if maxLeftSum + maxRightSum + root.val > self.maxSum:
            self.maxSum = maxRightSum + maxLeftSum + root.val 

        return max(root.val + maxLeftSum , root.val + maxRightSum) 

    def maxPathSum(self, root):
        """
        :type root: TreeNode 
        :rtype: int
        """
        self.helper(root)

        if root == None:
            return 0 

        return self.maxSum

root = TreeNode(2)
root.left = TreeNode(-1)
# root.right = TreeNode(0)
# root.left.left = TreeNode(5)
# root.right.right = TreeNode(-3) 

sol = Solution()
print(sol.maxPathSum(root))

'''
simple logic : 
a tree has a path which has node 
sum(nodes) in a path 
return max sum

a node can be in the path that yields max sum 

we have to decide what is max at every node 

so a node must get max sum from left side : maxLeftSum and from right side : maxRightSide 

node must say which is max
    either  
            maxLeftSum or
            maxRightSum or 
            root.val + maxLeftSum  or 
            root.val + maxRightSum or 
            root.val + maxLeftSum + maxRightSum 

make value of maxSUm = which ever is maximum among the above,
'''