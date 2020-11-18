'''
1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root):
        self.result = 0
        
        def height(root):
            if(not root):
                return 0

            left = height(root.left) + 1
            right = height(root.right) + 1
            
            return max(left,right)
        
        def dfs(root, depth, maxDepth):
			# leaf and height == maxDepth 
            if depth == maxDepth:
                self.result += root.val
                return None
		
            if root.left:
                dfs(root.left, depth+1, maxDepth) # return dfs() will return just 7 and doest execute the next statement 

            if root.right:
                dfs(root.right, depth+1, maxDepth)
        
        maxDepth = height(root)
        dfs(root,1,maxDepth)
        return self.result 

sol = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(7)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(8)

print(sol.deepestLeavesSum(root))