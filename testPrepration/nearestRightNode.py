'''
1602. Find Nearest Right Node in Binary Tree

Given the root of a binary tree and a node u in the tree, 
return the nearest node on the same level that is to the right of u, 
or return null if u is the rightmost node in its level.

Example 1:
Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node on the same level to the right of node 4 is node 5.

Example 2:
Input: root = [3,null,4,2], u = 2
Output: null
Explanation: There are no nodes to the right of 2.

Example 3:
Input: root = [1], u = 1
Output: null

Example 4:
Input: root = [3,4,2,null,null,null,1], u = 4
Output: 2

Constraints:
The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
All values in the tree are distinct.
u is a node in the binary tree rooted at root.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        
        if root == None:
            return None 
        
        queue = [(root,0)] # 1,0
        
        while queue:
            node, level = queue.pop(0) # node = 2, level = 1
            
            if node == u and len(queue) >= 1: # 2 
                nextNode, nextLevel = queue.pop(0) # 3,1 
                if nextLevel == level:
                    return nextNode
                
            if node:
                if node.left:
                    queue.append((node.left, level+1)) # 2, 1, none
                if node.right:
                    queue.append((node.right, level+1)) # 3, 1
                                      
        return None        

sol = Solution()
root = TreeNode(1) 
print(sol.findNearestRightNode(root, 1)) 