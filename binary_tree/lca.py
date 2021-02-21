class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __repr__(self):
        # return str(self.val)
        return f"TN(val={self.val})"

class Solution():
    def lowestCommonAncestor(self,root,p,q) :
        if root == None:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q) # 5, none, none
        right = self.lowestCommonAncestor(root.right, p, q) # none
        
        if left and right: 
            return root 
        
        if left:
            return left 
        
        if right:
            return right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

p = TreeNode(2)
q = TreeNode(3)

sol = Solution()
print(sol.lowestCommonAncestor(root,p,q))