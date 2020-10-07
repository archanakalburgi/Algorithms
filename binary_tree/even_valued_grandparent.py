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

    def evenGrandparent(self, root, parent = 1, grandparent = 1):
        if root:
            if grandparent % 2 == 0:
                self.tsum += root.val 
                # self.tsum = self.tsum + root.val
            # print('\n') 
            # print('node = '+str(root.val))
            # print('parent = '+str(parent))
            # print('grandparent = '+str(grandparent))
            # print(self.tsum)
            self.evenGrandparent(root.left, root.val, parent)  # node, parent, grandparent
            self.evenGrandparent(root.right, root.val, parent)  

    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # tsum = 0

        self.evenGrandparent(root)
        return self.tsum 

'''
1. what to send as node parent and grandparent ? 

2. if parent = 0 and grandparent = 0, 
    as soon as called condition gets executed even though actual grandparent is odd 
    0%2 = 0 : is true even if gp is an odd number but 
    we want it to change only if grandparent is even
    so make gp odd in the begining 

'''

root = TreeNode(6)
root.left = TreeNode(7)  
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.left.left.left = TreeNode(9) 
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4) 
root.right.left = TreeNode(1) 
root.right.right= TreeNode(3)
root.right.right.right = TreeNode(5) 

sol = Solution()
print(sol.sumEvenGrandparent(root))