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

class ExpTreeNode: # only construct the nodes of the tree 
    def __init__ (self, data): 
        self.element = data 
        self.left = None 
        self.right = None

class ExpressionTree: 
    def rec_build_tree(self, curNode, exp_q):
        token = exp_q.dequeue()

        if token == '(' :
            curNode.left = ExpTreeNode(None)
            self.rec_build_tree(curNode.left, exp_q)

            curNode.element = exp_q.dequeue()
            curNode.right = ExpTreeNode(None)
            self.rec_build_tree(curNode.right, exp_q) 

            exp_q.dequeue()

        else :
            curNode.element = token 

    def buildTree(self, expStr):
        exp_q = Queue()
        for token in expStr:
            exp_q.enqueue(token)

        self.expTree = ExpTreeNode(None)
        self.rec_build_tree(self.expTree, exp_q)

exp = ExpressionTree() 
exp.buildTree('((2*7)+8)') 