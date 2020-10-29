'''
class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, data):
        self.items.insert(0, data)

    def addRear(self, data):
        self.items.append(data)

    def removeFront(self):
        if self.items: 
            self.items.pop()

    def removeRear(self):
        if self.items:
            self.items.pop(0)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def size(self):
        return len(self.items)  

    def peekFront(self):
        return self.items[-1]

    def peekRear(self):
        return self.item[0] 
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


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = []
        q.append((root, 0))
        maxWidth = 0
        
        while q:
            size = len(q)
            maxWidth = max(maxWidth, q[-1][1] - q[0][1]) 
            for _ in range(size):
                node, index = q.pop(0)
                
                if node.left:
                    q.append((node.left, 2 * index))
                
                if node.right:
                    q.append((node.right, 2 * index + 1))
            
        return maxWidth 

root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(9) 
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
# root.right.right = TreeNode(6) 


sol = Solution()
print(sol.widthOfBinaryTree(root)) 