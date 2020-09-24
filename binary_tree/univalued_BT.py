'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
'''

# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root):
        """
        i/p: TreeNode
        o/p: True/False -> bool
        """
        def is_univalue(root):
        ''''
            if root == None :
                return True

            else:
                return is_univalue(root.left) and is_univalue(root.right)     

        if root == None :
            return True  
        else :
            val = root.val 
            return is_univalue(root)
        '''
# why??
         

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1) 
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5) 


sol = Solution()
print(sol.isUnivalTree(root)) 
