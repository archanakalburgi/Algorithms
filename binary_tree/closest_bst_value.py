'''
270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286
    
    4
   / \
  2   5
 / \
1   3

Output: 4
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def traverseTree(self, root, target, closestNode):
        if root == None :
            return closestNode 
        
    
        if abs(root.val - target) < abs(closestNode - target): 
            closestNode = root.val 

        if root.val > target :
            return self.traverseTree(root.left, target, closestNode) 

        else :
            return self.traverseTree(root.right, target, closestNode)

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root == None:
            return

        else :
            return self.traverseTree(root, target, root.val)


# (4, 2.7, 4): <- 3 
#     is 4 - 2.7 < 4 - 2.7 -> 1.3 < 1.3 : False

#     is 4 > 2.7 : True
#         traverseTree(2, 2.7, 4): <- 3
#             is 2 - 2.7 < 4 - 2.7 -> 0.7 < 1.3 : True
#                 closestNode = 2
            
#             is 2 > 2.traverseTree7 : False 

#             traverseTree(3, 2.7, 2) : <- 3
#                 is 3 - 2.7 < 2 - 2.7 -> 0.3 < 0.7 : True 
#                     closestNode = 3  

#                 is 3 > 2.7 : True
#                     traverseTree(None, 2.7, 3):
#                         return 3 

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

sol = Solution()
print(sol.closestValue(root,3.7))     


'''
new on BST : 

        4               : is a bst
      /   \ 
    2       5
  /   \
1       3


        4               : not a bst , 4 > 3 , 3 can't be on the right side of 4 
      /   \
    2       3 
  /    \          
1       5

''' 


