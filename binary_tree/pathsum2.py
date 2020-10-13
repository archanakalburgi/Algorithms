'''
113 

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, sum, nlist):  
    if root: 

        nlist + [root.val]

        if sum == root.val and root.left == None and root.right == None:   
            return nlist + [root.val] 

        else :
            left = pathSum(root.left, sum-root.val, nlist + [root.val])  
            right = pathSum(root.right, sum-root.val, nlist + [root.val]) 

        return [left] + [right] 

def pathSum2(root, sum, nlist, plist): # (1,7,[],[]), (2,6,[1],[]), (3,4,[1,2],[]), (4,4,[1,2],[]) ||||| (1,7,[],[1,2,4])
    if root : 

        nlist.append(root.val) # nlist = [1,2,3] [1,2,4] ||| [1], [1,6] 
        
        if sum == root.val and root.left == None and root.right == None: #t  t
            plist.append(nlist)  # plist = [1,2,4]| [1,2,4],[1,6] 
            '''
            concatenation won't work as we have change plist to keep the nodes 
            '''
        else:    
            pathSum2(root.left, sum - root.val, nlist, plist) # pathSum2(2,6,[1],[]) pathSum2(3,4,[1,2],[]) , pathSum2(none,4,[1,2,3],[])
            pathSum2(root.right, sum - root.val, nlist, plist) # pathSum2(4,4,[1,2],[]) , pathSum2(none,0,[1,2,4],[1,2,4]) |||||| pathSum2(6,6,[],[1,2,4])
            
        nlist.pop() 
        '''
        only remove the last node as leaf is reached and sum of nodes != sum 
        '''

    return plist  

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(6) 
root.left.left = TreeNode(3)
root.left.right = TreeNode(4) 
  

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(6) 
# root.left.left = TreeNode(4) 
     

# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
# root.left.left = TreeNode(11)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(1)  

print(pathSum2(root, 7, nlist=[], plist=[])) 
# print(pathSum(root,7,nlist=[]))