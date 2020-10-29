'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


'''

'''
abs(leftHeight - rightHeight) <= 1 

height = nodes - 1 

leftHeight = height(root.left) 
rightHeight = height(root.right) 

if abs(leftHeight - rightHeight) <= 1:
    return True  
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def height(self, root): 
        if root == None:
            return 0  
        
        left = self.height(root.left)
        right = self.height(root.right)
          
        return max(left, right) + 1 

    def isBalanced(self, root):
        if root == None:
            return True
        # print(self.height(root.left)) 
        # print (self.height(root.right)) 
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

root = TreeNode(1)
root.left = TreeNode(2) 
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)

sol = Solution()
print(sol.isBalanced(root)) 


'''
catch in the problem : 
    all subtrees must be balanced + (height of left - height of right) < 2

    1. calculate height of left and left trees 
    2. check if subtrees are balanced 
'''