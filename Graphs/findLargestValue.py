'''
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]


Example 2:

Input: root = [1,2,3]
Output: [1,3]

Example 3:

Input: root = [1]
Output: [1]


Example 4:

Input: root = [1,null,2]
Output: [1,2]


Example 5:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
'''

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def bfs(root,maxValues):
            # row = 0
            queue = [(root,0)]
            # largest = -999
            if root == None: # if skipped gives runtime error 
                return None 
            while queue:
                node, row = queue.pop(0)
                # largest = max(node.val, largest) 
                # maxValues.append(largest) 

                if node.left:
                    queue.append((node.left, row+1))
                if node.right:
                    queue.append((node.right, row+1))
                if row < len(maxValues):
                    maxValues[row] = max(maxValues[row], node.val)
                else:
                    maxValues.append(node.val)

                # print(row)
                # print(maxValues, len(maxValues)) 
        
        maxValues = []
        bfs (root, maxValues) 
        return maxValues 

root = TreeNode(1)
root.left = TreeNode(3) 
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

sol = Solution()
print(sol.largestValues(root)) 

'''
bfs 
collect max in a list 
return list 

but :
got to store highest values from each row 
keep track of each row

how to keep track of each row ?
keep track of index 
'''