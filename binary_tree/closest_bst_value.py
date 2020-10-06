'''
270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def traverseTree(self, root, target):
        if root == None :
            return 0
        closestNode = 0 
        left = self.traverseTree(root.left, target)
        right = self.traverseTree(root.right, target)

        if abs(float(left) - target) < abs(float(root.val) - target) :
            closestNode = left 

        if abs(float(right) - target) < abs(float(root.val) - target):
            closestNode = right 

        return closestNode 

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root == None:
            return

        else :
            return self.traverseTree(root, target)

        # def pickClosest(root, closest = 999): 
        #     if root == None:
        #         return
            
        #     else :
        #         left = pickClosest(root.left)
        #         right = pickClosest(root.right)
        #         if closest > target - root.val:
        #             closest = root.val 
        #         return closest 

        # if root == None:
        #     return 
        # else :
        #     return pickClosest(root, target)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

sol = Solution()
print(sol.closestValue(root,3.714286))    

            
