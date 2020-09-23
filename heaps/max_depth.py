'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Given binary tree [3,9,20,null,null,15,7],
return its depth = 3.


        3
      /   \
    /       \
    9       20
          /   \
         15     7

height = 1 (must case)
height_root = 1
height_left = 1
height_right = 2

total_height = height_root + max(height_left, height_right)
             1 + 2 
             3
'''



class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root, depth=1):
        '''
        if root == None :
            return 0
        if root:
            if root.left : # if a child of a node is encountered then the depth incereases by 1 
                depth += 1
                self.maxDepth(root.left, depth) 
            if root.right:
                depth +=1 
                self.maxDepth(root.right, depth)
        return max(1,depth)
        '''

        '''
        in the above, the depth is incremented when left, right child is incremented and depth is returned 
        '''

        if root == None :
            return 0
        else :
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right)) 
        
        '''
        every time maxDepth is returned 1 is added in the return statement 
        1 will be added reverse (each time the function is called) if a node has a left or a right child 
        '''
'''
        1
    2       3

max(self.maxDepth(root.left),self.maxDepth(root.right))

self.maxDepth(root.left) 
    self.maxDepth(2) -> 1 

self.maxDepth(root.right)
    self.maxDepth(3) -> 1

max(self.maxDepth(root.left),self.maxDepth(root.right)) = 1

return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))  = 1+1 = 2
'''


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)  

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)

sol = Solution()
print(sol.maxDepth(root))