# from queue import Queue
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
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None 

'''class BFS :
    def bfs_traversal(root):
        Queue q
        q.enqueue(root.data)
        while not q.is_empty():
            print(q.pop()) 
            if root.left:
                q.push(root.left)
            if root.right:
                q.push(root.right)

why it didn't work :
- trying to check the left and right children of the node that you have already taken out from the queue !!!

so store the popped value in a variable 
'''


class BFS :
    def bfs_traversal(self, root):
        q = Queue() # why do we have to put bracket while creating an instance of a class ?
        q.enqueue(root)
        traversal = [] 
        while not q.is_empty():
            x = q.dequeue()
            traversal.append(x.data) 
            if x.left: # in TB it says "if node.left is not None:" will it make any diff when written "if x.left:"
                q.enqueue(x.left)
            if x.right:
                q.enqueue(x.right)
        return traversal  

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
print(bfs.bfs_traversal(root)) 
