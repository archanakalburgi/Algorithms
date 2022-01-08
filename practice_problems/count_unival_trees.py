# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def count(self, root):
        if root.left == None and root.right == None:
            return (root.val, 1)
        else:
            lval, rval = None, None
            lcnt, rcnt = 0, 0
            
            if root.left is not None:
                lval ,lcnt = self.count(root.left)
                
            if root.right is not None:
                rval, rcnt = self.count(root.right)
                
            if root.val == rval and root.val == lval:
                return (root.val, lcnt + rcnt + 1)
            
            if root.left == None and root.val == rval:
                return (root.val, rcnt + 1)
            
            if root.right == None and root.val == lval:
                return (root.val, lcnt + 1)
            
            else:
                # print(f"r{root.val} - {rval, rcnt}, l{lval, lcnt}")
                return (None, lcnt+rcnt)
            
            
    def countUnivalSubtrees(self, root):
        if not root:
            return 0
        else:
            return self.count(root)[1]
        



# Rasika's version

def countRecur(self, curr):
    if curr is None:
        return (None, True)
    (left, isUniL) = self.countRecur(curr.left)
    (right, isUniR) = self.countRecur(curr.right)
    leftOk = False
    if (left is not None and isUniL and curr.val == left.val) or left is None:
        leftOk = True
        
    rightOk = False
    if (right is not None and isUniR and curr.val == right.val) or right is None:
        rightOk = True
        
    if leftOk and rightOk:
        self.count = self.count + 1
        return (curr, True)
    return (curr, False)
