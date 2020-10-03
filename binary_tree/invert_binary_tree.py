'''
226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9


Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

'''
    1           mirror image 
   / \
  2   3

    1
   / \
  3   2

1. construch new binary tree from nodes ???
post -> 2,3,1
pre -> 1,2,3 

- swap left and right 
temp = left
left = right 
right = temp 

- repeat the above for ull tree ??


'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # def swap(self, root):
    #     if root == None:
    #         return 

    #     temp = TreeNode()

    #     temp = root.left 
    #     root.left = root.right 
    #     root.right = temp 
    '''
    swaps left and right child ...
    problem -> swap full tree 
    '''

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        else:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            root.left = right
            root.right = left 
        
            return root  


            # invertTree(1):
            #     left =  invertTree(2)
            #                 left =  invertTree(4)
            #                             left = invertTree(None)
            #                                         left = None  
            #                             #left = None
            #                 right = invertTree(4) 
            #                             left = invertTree(None)
            #                                         left = None 
            #                                         right = invertTree(None)
            #                                                     right = None
            #                                         right = None 

            #                                         left = None
            #                                         right = None 

            #                                         return 4
            #                 left = 4 

            #                 right = invertTree(5) 
            #                             left = invertTree(None)
            #                                         left = None
            #                                         right = invertTree(None)
            #                                         right = None 

            #                                         left = None 
            #                                         right = None 
                                                    
            #                                         return 5
            #                 right = 5 

            #                 left = 5
            #                 right = 4

            #                 return 2
                
            #     left = 2
                
            #     right = invertTree(3)
            #                 left = invertTree(None)
            #                             left = None 
            #                             return None
            #                 left = none 
            #                 right = invertTree(None)
            #                             return None 
            #                 right = None 

            #                 left = None 
            #                 right = None

            #                 return 3 
            #     right = 3
                
            #     left = 3
            #     right = 2 

            #     return 1 

            
                    
root = TreeNode(1)

root.left  = TreeNode(2) 
root.right = TreeNode(3)

root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 

sol = Solution()
print(sol.invertTree(root))  
        
