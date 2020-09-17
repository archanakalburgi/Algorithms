class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None 

class Solution:

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
     
        return [root.data] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# root = [1,null,2,3]
'''
    1
        2
    3
''' 
root = TreeNode(1)
root.left = None
root.right = TreeNode(2)
root.right.left = TreeNode(3)   

# root = TreeNode(root)
sol = Solution()
print(sol.preorderTraversal(root))  







'''
def preorderTraversal(root):
    def node(val=0, left=None, right=None):
        val = val
        left = left
        right = right 
    if root is not None:
        preorderTraversal(root.val)
        preorderTraversal(root.left)
        preorderTraversal(root.right) 
'''


