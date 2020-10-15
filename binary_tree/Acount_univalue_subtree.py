'''
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

 

Example 1:

    Input: root = [5,1,5,5,5,null,5]
    Output: 4
'''



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countUnivalSubtrees(self, root, count=0): 
        if root == None :
            return True 
        
        left_subtree = self.countUnivalSubtrees(root.left, count) 
        right_subtree = self.countUnivalSubtrees(root.right, count) 

        if left_subtree and right_subtree and 
            count = count + 1
            print(self.count) 
            return True 
            
        return count 


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
root.right.right = TreeNode(5)

sol = Solution()
print(sol.countUnivalSubtrees(root))  
    