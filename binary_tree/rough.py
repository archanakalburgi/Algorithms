'''
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different 
nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)


eg:

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

    def diff(self, root, minValue = 9999, maxValue = 0 ):
        if root == None:
            return 0 
        
        left = self.diff(root.left, minValue, maxValue)
        right = self.diff(root.right, minValue, maxValue)

        if root.val < minValue:
            minValue = root.val 

        if root.val > maxValue:
            maxValue = root.val 

        return max(maxValue - minValue, left, right)  

    def maxAncestorDiff(self,root):

        if root == None:
            return 0 

        return self.diff(root)  

diff(8,9999,0)
    l = diff(3,9999,0)
        l = diff(1,9999,0)
            l = diff(None, 9999, 0)
            l = 0 
            r = diff(None, 9999, 0)
            r = 0
            1 < 9999 : False 
            1 > 0 : True 
            maxValue = 1 
            return max(1-9999, 0, 0)
        

root = TreeNode(8)
root.left  = TreeNode(3) 
root.right = TreeNode(10)

root.left.left = TreeNode(1) 
root.left.right = TreeNode(6)

root.left.right.left= TreeNode(4)
root.left.right.right = TreeNode(7)

root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13) 

sol = Solution()
print(sol.maxAncestorDiff(root))


'''
class Solution1(object):
    res = 0
    # def __init__(self):
        # self.minValue = 0
        # self.maxValue = 9999

    def calculateDiff(self, root, maxValue = -999, minValue = 999):
        if root == None:
            return 0
             

        left = self.calculateDiff(root.left, max(maxValue, root.val), min(minValue, root.val))  
        right = self.calculateDiff(root.right, max(maxValue, root.val), min(minValue, root.val))
 
        if root.val > minValue:
            minValue = root.val

        if root.val > maxValue:
            maxValue = root.val 

        self.res = abs(maxValue - minValue)

        return 

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.calculateDiff(root)

        if root == None:
            return 0

        else:
            return self.res 
'''

