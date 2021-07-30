'''
513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        def dfsTraverse(root, previousLevel, currentLevel):
            if root == None:
                return None
            
            if currentLevel > previousLevel[0]:
                previousLevel[0] = currentLevel 
                previousLevel[1] = root.val
             
            dfsTraverse(root.left, previousLevel, currentLevel+1)
            dfsTraverse(root.right, previousLevel, currentLevel+1)

        previousLevel = [-1, None]
        dfsTraverse(root, previousLevel, 0) 
        return previousLevel[1] 

root = TreeNode(11)
root.left = TreeNode(12)
root.right = TreeNode(13)
root.right.left = TreeNode(14) 

sol = Solution()
print(sol.findBottomLeftValue(root)) 
            
'''
calculating height of tree
compare right/left height to height of tree
if rightHeight == height : return root.right
if leftHeight == height : return root.right 

fundamental flaw in above:
it returns just the immediate right child/ left child of the root node 
do not reach the bottom og the tree 
we need bottom left value
cannot be obtained 

overcoming :
track the currentLevel you are on, for every recursive call 
increment a varibale value eatch time you call the recursive fun 
this keeps record of currentLevel 
on every recurcive call compare currentLevel to maxHeight of the tree 

if maxHeight == currentLevel 
    return node.val

***** the level I am on and the previous level *****
'''