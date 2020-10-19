'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

'''
    3
   / \
  9  20
    /  \
   15   7

1. root = 3

2. root.left  = 9 
3. root.left.left = None 
4. root.left.right = None 

4. root.right = 20
5. root.right.left = 15 
6. root.right.right = 7

7. root.right.left.left = None 
8. root.right.left.right = None 

return true 


1. calculate depth/height of left subtree
2. calculate height of right subtree
3. if height(left subtree) = height(right subtree)+1: 
        return True 
    else : 
        return False 
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height (root):
            # count = 0
            if root == None:
                return True 

            else:
                left = height(root.left) 
                right = height(root.right)
                return max(left,right)+1 
       
        if root == None :
            return True   

        else :
            height_left = height(root.left)
            height_right = height(root.right)
            if abs(height_left - height_right) > 1:
                return False
            else :
                return self.isBalanced(root.left) and self.isBalanced(root.right) 
            
            # return height_left or height_right or height_right == height_left + 1 or height_left == height_right + 1 

root = TreeNode(1)

root.left  = TreeNode(2) 
 
root.right = TreeNode(2)
root.left.left = TreeNode(3) 
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4) 
root.left.left.right = TreeNode(4) 

sol = Solution()
print(sol.isBalanced(root)) 

