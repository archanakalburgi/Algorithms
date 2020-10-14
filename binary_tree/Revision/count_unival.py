'''
250. Count Univalue Subtrees

Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Example 1: 

Input: root = [5,1,5,5,5,null,5]
Output: 4


Example 2:

Input: root = []
Output: 0


Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
'''


'''
remember :

base case : last node must not have children 
            if a node is leaf i.e has no children then it is a unival subtree and so increment count (this is the decision taken at the leaf)
all the childrens of a node must have same value + node and it's children must have same value 

possibilities of getting None ??
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    '''
            1**
          /    \
        1 *      1
      /
    1       
    '''
    def countUnivalSubtrees(self, root): 
        self.count = 0

        def countUnival(root): 
            if root == None:
                return True 
            
            left = countUnival(root.left) 
            right = countUnival(root.right) 
            
            if left and right: 
                if root.left == None and root.right == None: 
                    self.count += 1
                    return True

                if root.right and root.left == None: 
                    if root.val == root.right.val:
                        self.count += 1
                        return True

                if root.left and root.right == None: 
                    if root.val == root.left.val:  
                        self.count += 1 
                        return True 

                if root.left and root.right:
                    if root.val == root.right.val == root.left.val:  
                        self.count += 1
                        return True
            
            return False
            
        countUnival(root)
        
        return self.count
        

root = TreeNode(5)
root.left = TreeNode(1) 
root.right = TreeNode(5)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
root.right.right = TreeNode(5)

sol = Solution()
print(sol.countUnivalSubtrees(root))  