'''
958. Check Completeness of a Binary Tree

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:

Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.



Example 2:

Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:

The tree will have between 1 and 100 nodes.
'''

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,item): 
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None  

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items) 

    def is_empty(self):
        if self.items:
            return False
        return True


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

class Solution(object):
    def isCompleteTree(self, root):
        q = Queue()
        q.enqueue(root)
        checkNode = False

        while not q.is_empty():
            x = q.dequeue()

            if x == None :
                checkNode = True
            
            else :
                if checkNode:
                    return False

                q.enqueue(x.left)
                q.enqueue(x.right) 
        
        return checkNode 

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6) 

sol = Solution()
print(sol.countNodes(root)) 

