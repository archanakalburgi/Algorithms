'''
662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. 
The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes 
(the leftmost and right most non-null nodes in the level, 
where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4

Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).


Example 2:
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2

Explanation: The maximum width existing in the third level with the length 2 (5,3).


Example 3:
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2

Explanation: The maximum width existing in the second level with the length 2 (3,2).


Example 4:
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8

Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
 

Constraints:

The given binary tree will have between 1 and 3000 nodes.
'''

'''
size = 0
q.add(root.val)
node = q.pop()
q.add(node.left)
q.add(node.right) 
size = max(len(q), size) 
node = q.pop() 
size = max(len(q), size)
node.left == node.right == None:
    return size 

keep track of the indices : 
    for example : if you know the index of extreme left node and extreme right node of the widest level 
    maximum width = index(extreme left node) - index(extreme right node)

how? 
    queue ???

'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
          1
         / \
        3   2 
       /        
      5     
    '''
    def widthOfBinaryTree(self, root): # widthOfBinaryTree(1)
        q = [] # []
        q.append((root, 0)) # q = [(1,0)]
        maxWidth = 0 # mwidth = 0
        
        while q: # q = [(1,0)] | q = [(3,0),(2,1)] q = (3,0)  | q = [5,0] | q = []

            size = len(q) # size = 1 , size = 2 , size = 1 
            maxWidth = max(maxWidth, q[-1][1] - q[0][1]+1) # maxWidth = max(0, 0-0+1) = 1 | maxWidth = max(1,1-0+1) = 2 | maxWidth = max(2,0-0+1) = 2
                                                # in case of just 1 node width = 1, so 1 is added 
            for i in range(size): # i = 0 | i = 0 , i = 1 | i = 0
                node, index = q.pop(0) # node,index = (1,0) | node,index = (3,0) , node,index = (2,1) | node,index = (5,0)
                
                if node.left: # t | t , f | f
                    q.append((node.left, 2 * index)) # q = [(3,0)] | q = [(5,0)]
                
                if node.right: # t | f , f | f
                    q.append((node.right, 2 * index + 1)) # q = [(3,0), (2,1)] 
            
        return maxWidth # returns 2 

root = TreeNode(1)
# root.left = TreeNode(3)
# root.left.left = TreeNode(5)
# root.left.left.left = TreeNode(9) 
# root.left.right = TreeNode(3)
# root.right = TreeNode(2)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(6) 


sol = Solution()
print(sol.widthOfBinaryTree(root)) 
                

'''
mistakes :
    jumped directly to implementing queue as bfs striked after reading 'width' 

got stuck : 
    emptying queue as required 

    overcame by : using for loop and emptying the queue accoringly and as required 
'''