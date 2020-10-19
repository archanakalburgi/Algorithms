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
'''
root.val        value           diff            closest = min(root.val-val , diff)          returnValue
4               3.7143          0.2857          0.2857                                          4
2               3.7143          1.7143          0.2857                                          4
1               3.7143          2.7143          0.2857                                          4
3               3.7143          1.2857          0.2857                                          4 
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # closest = 0
    def fetchClosestValue(self, root, target, closest):
        if root == None:
            return closest

        if abs(root.val - target) < abs(closest - target):
            closest = root.val 

        if target < root.val:
            return self.fetchClosestValue(root.left, target, closest) 
        
        return self.fetchClosestValue(root.right, target, closest) 
        
    
    def closestValue(self, root, target):
        # self.fetchClosestValue(root, target, closest)
        if root == None:
            return 0
        return self.fetchClosestValue(root,target, root.val)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

sol = Solution()
print(sol.closestValue(root,3.714286))


'''
when on the 2nd node in the tree, 1st node will be store in closest 
this repeats 
'''

        