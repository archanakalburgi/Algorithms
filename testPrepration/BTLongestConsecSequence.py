'''
298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the 
tree along the parent-child connections. The length consecutive path need to be 
from parent to child (cannot be the reverse).

Example 1:
Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
* it is not 3-2-1 because you cannot have a reverse sequence 
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def dfs(self, root, pathLength, parent):
        
            self.length = max(self.length, pathLength) 
            
            if root == None:
                return None
            
            if parent.val - root.val == -1: # checking the consecutiveness 
                pathLength += 1
            
            else:
                pathLength = 1
                
            self.dfs(root.left, pathLength, root)
            self.dfs(root.right, pathLength, root)

    def longestConsecutive(self, root):
        self.length = 0
        if root:
            self.dfs(root, 1, root)
        return self.length
        

# root = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(2)
# root.right.left.left = TreeNode(1)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

sol = Solution()
print(sol.longestConsecutive(root)) 