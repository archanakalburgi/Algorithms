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
        def helper(root, maxValues):
            queue = [(root,0)]
            if root == None:
                    return None
            while queue:
                node, level = queue.pop(0)

                if root.left:
                    queue.append((root.left, level+1))
                if root.right:
                    queue.append((root.right, level+1))

                if level < len(maxValues):
                    maxValues[level] = max(maxValues[level], node.val)  
                    # eg: on 2nd row if right child > left child, 
                    # right child will get appened instead of previously appended left child
                else:
                    maxValues.append(node.val) 
        
        maxValues = []
        helper(root, maxValues) 
        return maxValues

root = TreeNode(1)
root.left = TreeNode(2)
root.right =  TreeNode(3)

sol = Solution()
print(sol.largestValues(root))
