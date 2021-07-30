'''
Given a binary tree, return the sum of values of its deepest leaves.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(root):
            if root == None:
                return 0

            left = height(root.left)+1
            right = height(root.right)+1

            return max(left, right) 

        def sumOfDeepestLeaves(root, level):
            if root.left == None and root.right == None and depth == level:
                self.summ = self.summ + root.val
            
            if root.left:
                sumOfDeepestLeaves(root.left, level+1)
            if root.right:
                sumOfDeepestLeaves(root.right, level+1) 
        
        self.summ = 0
        depth = height(root) 
        sumOfDeepestLeaves(root, 1)

        return self.summ 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sol = Solution()
print(sol.deepestLeavesSum(root)) 

'''
height func
    left = height(root.left)+1 
    # because a left child already contributes to the height 

while passing level, level=1 since root is the 1st level  
'''