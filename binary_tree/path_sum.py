'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''
'''
target = 10
array = [1,2,3,4,5,6,7,8,9]
10-1 = 9
9-2 = 7
7-3 = 4
4-4 = 0 

target is exhausted when it reaches 4 
so sum of all numbers till 4 = target (1+2+3+4 = 10) 

1. visit a node 
2. store the value of the node 
3. substract the value of the node from the target 
3. check if target = 0 
4. return all the nodes sored / return true 
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None :
            return False 
        elif root.left == None and root.right == None and sum-root.val == 0 : # 20 = 5+4+11 -> still returns, 11 is not leaf 
            return True 
        else :
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)   
            
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8) 
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13) 
root.right.right = TreeNode(4) 
root.right.right.right =  TreeNode(1)

sol = Solution()
print(sol.hasPathSum(root, 20)) 