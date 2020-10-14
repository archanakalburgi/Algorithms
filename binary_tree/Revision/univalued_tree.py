'''
965. Univalued Binary Tree

A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:

Input: [1,1,1,1,1,null,1]
Output: true


Example 2:
 
Input: [2,2,2,5,2]
Output: false
 

Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
'''


'''
problem defination : 
    all nodes mush have same value in them -> return True, else return -> False

input output : tree , bool 
   1. input :
            1
        1       1

    output :
    True

    2. input 
        1
    1       2

    output :
    False 

pseudo code :
    func(root):
        if root == None:
            return True             
        
        left = root.left.val == root.val and func(root.left)
        right = root.right.val == root.val and func(root.right)

        return left and right 
        
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isUnivalTree(self, root):     
        left = root.left == None or root.left.val == root.val and self.isUnivalTree(root.left)
        right = root.right == None or root.right.val == root.val and self.isUnivalTree(root.right)

        return left and right 

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1) 
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1) 


sol = Solution()
print(sol.isUnivalTree(root)) 


'''
even if we encounter a null node it does not count 
'''