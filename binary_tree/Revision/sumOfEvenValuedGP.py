'''
1315. Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
(A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.

'''

'''
READ THE PROBLEM DEFINATION PROPERLY !!!!
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    sumOfNodes = 0
    def calculatingSum(self, root, parent, grandparent):
        if root == None:
            return 0
        
        else:

            if grandparent % 2 == 0:
                self.sumOfNodes = self.sumOfNodes + root.val 
            
            self.calculatingSum(root.left, root.val, parent) # keeps calling itself, top to bottom 
            self.calculatingSum(root.right, root.val, parent)

    def sumEvenGrandparent(self, root):
        self. calculatingSum(root, parent=1, grandparent=1)
        if root == None:
            return 0 
        return self.sumOfNodes 

        
    

root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(5)

sol = Solution()
print(sol.sumEvenGrandparent(root)) 