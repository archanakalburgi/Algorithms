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
left path should give the count of nodes of the longest path leftCount 
right path should give the count of nodes of the longest path rightCount 
top root should tell leftCount+rightCOunt+root -> this is the diameter of the tree, keep a tack of this
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    numOfNodes = 0 

    def heightOfSubtree(self, root):
        if root == None:
            return 0 

        else :
            leftHeight = self.heightOfSubtree(root.left) 
            rightHeight = self.heightOfSubtree(root.right)

            self.numOfNodes = max(self.numOfNodes, leftHeight + rightHeight + 1) 

            return max(leftHeight, rightHeight) + 1  

    def diameterOfBinaryTree(self, root): 
        if root == None:
            return 0 
        
        self.heightOfSubtree(root)
        return self.numOfNodes - 1 # height = no of nodes - 1  


root = TreeNode(9)
root.left = TreeNode(8)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(6)
root.left.right.left.left = TreeNode(1) 


sol = Solution()
print(sol.diameterOfBinaryTree(root))  

'''
* problem req : height 
height = no of nodes - 1 
easy to cal no of nodes 
calculate no of nodes 
return no of nodes - 1


first trial ::
    was failing to keep the count of the maximum no of nodes from left and right at every node 
        -> make use of a global variable to do so 
'''