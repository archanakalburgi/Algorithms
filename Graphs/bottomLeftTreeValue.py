'''
513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1
Example 2: 

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.

'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        if root == None:
            return None
        
        queue  = [root] # q = [2]
        # queue.append(root)
        
        while queue: # [2] , [1,3] 
            bottomLeftValue = queue[0].val # val = 2 , val = 1
            # print(bottomLeftValue) 
            tempQueue = [] # temp = [] , temp = []
            for node in queue: # node = 2, node = 1, node = 3
                if node.left: # true , false , false 
                    tempQueue.append(node.left) # temp = [1]
                if node.right: # true , false , false 
                    tempQueue.append(node.right) # temp = [1,3]
            
            queue = tempQueue # q = [1,3], q = []
        return bottomLeftValue # 1  

# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3) 

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


sol = Solution()
print(sol.findBottomLeftValue(root)) 