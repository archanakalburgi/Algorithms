'''
222. Count Complete Tree Nodes


Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''

''' 
is it a complete binary tree?
    must not have a null node till the end- bfs traversal 

    no node after a null node 
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
    def countNodes(self, root):
        q = Queue()
        q.enqueue(root)
        count = 0
        check_null = False
        
        while not q.is_empty():
            x = q.dequeue()

            if x == None :
                check_null = True
            
            else :
                count = count + 1
                if check_null:
                    return 'Not a CBT' 

                q.enqueue(x.left)
                q.enqueue(x.right)  
   
        return count

root = TreeNode(1)
root.left = TreeNode(2) 
root.right = TreeNode(3)

sol = Solution()
print(sol.countNodes(root)) 



class Solution1(object):
    count = 0
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root):
            # count = 0
            if root :
                self.count = self.count + 1
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)
        return self.count 

sol1 = Solution1()
print(sol1.countNodes(root)) 