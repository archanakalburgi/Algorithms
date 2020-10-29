'''
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B 
where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)



Example 1:
    Input: [8,3,10,1,6,null,14,null,null,4,7,13]
    Output: 7
    Explanation: 
    We have various ancestor-node differences, some of which are given below :
    |8 - 3| = 5
    |3 - 7| = 4
    |8 - 1| = 7
    |10 - 13| = 3
    Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # maxVal = 999
    maxDiff = -999

    def AncestorDiff(self, root, minVal = 999, maxVal = -999):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        else :
            maxVal = max(maxVal, root.val) 
            minVal = min(minVal, root.val)
            self.maxDiff = max(maxVal - minVal, self.maxDiff)  
            return max(self.AncestorDiff(root.left, minVal, maxVal), self.AncestorDiff(root.right, minVal, maxVal)) 

        
    def maxAncestorDiff(self, root):
        self.AncestorDiff(root)
        if root == 0:
            return 0
        else: 
            return self.maxDiff

root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1) 
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7) 
root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13) 

sol = Solution()
print(sol.maxAncestorDiff(root)) 