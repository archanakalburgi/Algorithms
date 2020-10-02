'''
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

'''
        1
      /   \
     2     3

- diameter = longest path = distance from 2 to 3 = 2 (no of edges traversed = 2)

- 1 edge = 2 nodes 
so, no of nodes = no of edges + 1

no of edges = no of nodes - 1

- diameter of left 

- distance from extreme left leaf to extreme right ? (again depth) 


            1 [2]
         /     \
    [1] 2       3 [1]
     /     \     
[0] 4       5 [0]


1. right height + left height (few cases )
2. if only left -> left height 
3. if only on right -> right height 
'''

'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None :
            return 0 
        
        left = self.height(root.left) # 2, 1, 0
        right = self.height(root.right) # 1, 1, 0 

        left_dia = self.diameterOfBinaryTree(root.left) # 0,  
        right_dia = self.diameterOfBinaryTree(root.right) # 0

        return max(left + right, max(left_dia, right_dia))

    def height(self,root):
        if root == None :
            return 0
        else :
            return 1 + max(self.height(root.left), self.height(root.right)) 
 

root = TreeNode(1)

root.left  = TreeNode(2) 
root.right = TreeNode(3)

root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 

sol = Solution()
print(sol.diameterOfBinaryTree(root)) 
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    final_max = 0 
    def diameterOfBinaryTree(self, root):
        if root == None :
            return 0
        else :
            left = self.diameterOfBinaryTree(root.left) 
            right = self.diameterOfBinaryTree(root.right) 

            if (left + right + 1) > self.final_max:
                self.final_max = left + right + 1
            
            return max(1+left, 1+right)  

root = TreeNode(1)

root.left  = TreeNode(2) 
root.right = TreeNode(3)

root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 

sol = Solution()
print(sol.diameterOfBinaryTree(root)) 


'''
i am 1 
some asks i'll ask person below me and add 1 to that value (1 being me) and say x value and say I am max 

but one the other person has x value he checks with previous maximum value if x is max he updates maximum 

        finally we have true maximum 

then i will return max of left and right child + 1 (one being me) 
'''