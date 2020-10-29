'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

'''

'''
mirror image = 
centre remains same 
left become right 
right becomes left 
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def isMirror(self, leftSubtree, rightSubtree):
        if leftSubtree == None and rightSubtree == None :
            return True

        return (leftSubtree.val == rightSubtree.val) and self.isMirror(leftSubtree.right, rightSubtree.left) and self.isMirror(leftSubtree.left, rightSubtree.right)

    def isSymmetric(self,root):
        return self.isMirror(root, root) 


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

sol = Solution()
print(sol.isSymmetric(root))
       