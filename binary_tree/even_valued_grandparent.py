'''
1315. Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
(A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):
    tsum = 0

    def evenGrandparent(self, root, parent, grandparent):
        if root:
            if grandparent :
                self.tsum = self.tsum + root.val 
                self.evenGrandparent(root.left, root.val%2 == 0, parent) 
                self.evenGrandparent(root.right, root.val%2 == 0, parent) 

    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # tsum = 0

        self.evenGrandparent(root, False, False)
        return self.tsum 

root = TreeNode(6)
root.left = TreeNode(7) 
root.right = TreeNode(2)
root.left.left = TreeNode(7)
root.left.right = TreeNode(7)
root.left.left.left = (9) 

root.right.left = TreeNode(1) 
root.right.right= TreeNode(3)
root.right.right.right = TreeNode(5) 

sol = Solution()
print(sol.sumEvenGrandparent(root))