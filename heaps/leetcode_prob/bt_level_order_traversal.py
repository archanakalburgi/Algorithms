'''
https://github.com/anupkalburgi/snippets/blob/master/python/olgish/binary_tree.py
'''

class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None 



class Solution :
    '''
                3
            /       \
            9       20
                /       \
                15      7 
    '''
    def levelOrder(self, root): # root = 3, 9
        if root is None:
            return []
        
        first_level = [root] # first_level = [3]
        next_level = []
        level = []
        result = []

        while first_level != []: # first_level = [3] , [9,20], [15,7], [] 
            for root in first_level: # root = 3 , 9 , 20 , 15 , 7 
                level.append(root.data) # level = [3], [9,20], [15,7]
                if root.left is not None:
                    next_level.append(root.left) # next_level = [9], [15], [], []
                if root.right is not None: 
                    next_level.append(root.right) # next_level = [9,20] , [15,7], [], []
            result.append(level) # result = [[3],[9,20], [15,7]] 
            level = [] # level = [], [] , []
            first_level = next_level # first_level = [9,20], [15,7], [] 
            next_level = [] # next_level = [],[], []
        return result 

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)  

sol = Solution()
print(sol.levelOrder(root))  

'''
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2
node1.left = TreeNode(4)
node1.right = TreeNode(5)
node2.left = TreeNode(6)
node2.right = TreeNode(7)
node1.right.left = TreeNode(8)
node2.right.left = TreeNode(9)
node2.right.right = TreeNode(10) 

bfs = BFS() 
print(bfs.bfs_traversal(root)) '''

