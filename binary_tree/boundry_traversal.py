'''
        20
      /    \
     8      22
   /   \      \
  4     12     25
       /   \
      10   14 


traversal = [20,8,4,10,14,25,22] 

input :
        1
       / \
      2   3
     / \
    4   5

output :
    1,2,4,5,3

root:                   1
    print -> root.val   

left:                   2,3
    go down to left 
    print -> root.val
    go down to left 
    print -> root.left
    till root.left == None  

leaf:                  4,5
    left leaves:
        go down to right 
        go down to right 
        print right node if root.left and root.right == None 

    right leaves
        print root.val
        go up to print if any  

right: 
    print 3 

'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printBoundryLeft(root):
    if root :
        if root.left :
            print(root.val)
            printBoundryLeft(root.left) 

def printBoundryLeaves(root):
    if root :
        printBoundryLeaves(root.left)

        if root.left == None and root.right == None:
            print(root.val)

        printBoundryLeaves(root.right) 

def printBoundryRight(root):
    if root :
        if root.right:
            printBoundryRight(root.right) 
            print(root.val)

def boundryTraversal(root): 
    if root :
        print(root.val)

        printBoundryLeft(root.left)

        printBoundryLeaves(root.left)
        printBoundryLeaves(root.right)

        printBoundryRight(root.right) 


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5) 


# root = TreeNode(20)
# root.left = TreeNode(8)
# root.right = TreeNode(22)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(12) 
# root.left.right.left = TreeNode(10)
# root.left.right.right = TreeNode(14)
# root.right.right = TreeNode(25) 

boundryTraversal(root) 