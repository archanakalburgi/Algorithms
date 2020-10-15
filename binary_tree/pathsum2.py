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

def pathSum(root, sum, nlist, all_paths):  
    if root == None:  
        return all_paths

    else :
         
        if root.val == sum and root.left == None and root.right == None:   
            return all_paths + [nlist + [root.val]] 

        else :
            left = pathSum(root.left, sum - root.val, nlist + [root.val] , all_paths)  
            right = pathSum(root.right, sum - root.val, nlist + [root.val] , all_paths) 

        return left + right 

'''
    calls        nlist + [root.val]          changes made in that call 
      1            []                           [1]
      2            [1]+[2]                      [1,2]
      3            [1,2]+[3]                    [1,2,3]
      4            [1,2,3]                      [1,2]
      5            [1,2]                        [1,2,4] 
      6            [1]                          [] 

pathSum(1,7,[],[]):------------1
    left = pathSum(2,6,[1],[])--------------2
            left = pathSum(3,4,[1,2],[])-----------3
                    pathsum(none,1,[1,2,3],[])------------4
                        left = []   # all_paths     (here we get empty path because we have not hit the right path that satisfies the condition)
        right =  pathSum(4,4,[1,2],[])--------------------5
                return all_paths + [nlist + [root.val]]
                return [] + [[1,2] + [4]]    
                right = [[1,2,4]] 

        return left+right = [] + [[1,2,4]] = [[1,2,4]] 
    left = [[1,2,4]]
    right = pathSum(6,6,[1],[[1,2,4]])--------------6 
            return all_paths + [nlist + [root.val]]
            return [] + [[1] + [6]]
            return [] + [[1,6]]
            return [] + [[1,6]] 
            return [[1,6]]
    right = [[1,6]]

    return left + right 
    [[1,2,4]] + [[1,6]]
    [[1,2,4],[1,6]] 
'''


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(6) 
root.left.left = TreeNode(4)
root.left.right = TreeNode(3) 
root.left.right.right = TreeNode(1)

print(pathSum(root,7,[], [] )) 