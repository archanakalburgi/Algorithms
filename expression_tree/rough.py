class ExpTreeNode:  
    def __init__ (self, data): 
        self.element = data 
        self.left = None 
        self.right = None


class ExpressionTree :
    def evaluate(expStr):
        # expStr = '((2*7)+8)'
        root = ExpTreeNode(data = None) 
        current_node = root # root, curent_node 
        count = 0 
        for exp in expStr : # 7 , ) 
            count = count + 1 
            if exp == '(' :
                current_node.left = ExpTreeNode(data=None) 
            if exp >= '0' and exp <= '9':
                current_node = exp 
            if exp == '+' or exp == '-' or exp == '*' or exp == '/' :
                # move up to the parent -> ?
                current_node = exp 
                current_node.right = ExpTreeNode(data=None)
            if exp == ')':
                current_node = expStr[int(count-1/2)] # 5-1/2 = 2 

        
        return current_node

expStr = '((2*7)+8)'
print(ExpTreeNode.evaluate(expStr)) 

'''
        None
    *           
2       7


q = ['(','(','2','*','7',')','+','8',')']
'''