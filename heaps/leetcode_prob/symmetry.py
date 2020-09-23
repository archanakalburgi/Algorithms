'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


conditions :
   1. root.left.right  == root.right.left  
   2. root.left.left == root.right.right  


'''

class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None 



class Solution :
    def is_symmetric(self, left, right):
        if left and right :
            # must check the complete left subtree and right subtree  
            return left.data == right.data and self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left) 
        return left == right

    def isSymmetric(self, root):
        if root == None :
            return True 

        return self.is_symmetric(root.left, root.right) 


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

sol = Solution()
print(sol.isSymmetric(root)) 