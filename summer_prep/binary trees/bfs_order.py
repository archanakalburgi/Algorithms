class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root):
        q, level = [], []
        q.append([root])
        level = q.pop()
        level_len = len(level)
        node = level[0]
        
        level.append(node.left)
        level.append(node.right)
        
        q.append(level)
        
        return q
        
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)


s = Solution()
result = s.levelOrder(root)
for res in result:
    # for r in res:
    print(res)
# print(res) 