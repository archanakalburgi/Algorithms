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

'''
        8
      /   \
    3      10


diff(8, 9999, 0):
    8 < min -> 9999 : True
        min = 8 
    8 > max -> 0 : True
        max = 8 
    return max(0 -> 8-8, diff(3, 8, 8), diff(10, 8, 8))  <- max(0, 5, diff(10, 8, 8))  <- max(0, 5, 2) <- 5 
        diff(3, 8, 8):
            is 3 < min -> 8 : True
                min = 3
            is 3 > max -> 8 : False 
            return max(5 -> 8-3 , diff(None,3,8) , diff(None, 3,8)) <- max(5, 0, diff(None, 3, 8)) <- max(5,0,0) <- 5 
                diff(None, 3, 8):
                    return 0
                                                                        diff(10, 8, 8):
                                                                            is 10 < 8 : False  
                                                                            is 10 > 8 : True 
                                                                                max = 10
                                                                            return max(10-8 -> 2, diff(None, 8, 10), diff(None, 8, 10)) <- max(2,0,0) <- 2
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
        
        if root.val < minValue:
            minValue = root.val 

        if root.val > maxValue:
            maxValue = root.val 

        return max(maxValue - minValue, self.diff(root.left, minValue, maxValue), self.diff(root.right, minValue, maxValue))  

    def maxAncestorDiff(self,root):

        if root == None:
            return 0 

        return self.diff(root)  

                                                                        

root = TreeNode(8)
root.left  = TreeNode(3) 
root.right = TreeNode(10)

# root.left.left = TreeNode(1) 
# root.left.right = TreeNode(6)

# root.left.right.left= TreeNode(4)
# root.left.right.right = TreeNode(7)

# root.right.right = TreeNode(14)
# root.right.right.left = TreeNode(13) 

sol = Solution()
print(sol.maxAncestorDiff(root))
