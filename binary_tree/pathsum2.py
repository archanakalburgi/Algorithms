'''
113 

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, sum, nlist, all_paths):  
    if root == None:
        return []

    else :
         
        if root.val == sum and root.left == None and root.right == None:   
            return all_paths + [nlist + [root.val]] 

        else :
            left = pathSum(root.left, sum - root.val, nlist + [root.val] , all_paths)  
            right = pathSum(root.right, sum - root.val, nlist + [root.val] , all_paths) 

        return left + right 



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(6) 
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

print(pathSum(root,7,[], [] )) 