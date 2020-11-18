'''
1123. Lowest Common Ancestor of Deepest Leaves

Given the node of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the node of the tree is 0. if the depth of a node is d, 
the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, 
is the node A with the largest depth such that every node in S is in the subtree with node A.
Note: This question is the same as 865:
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/


Example 1:

Input: node = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but 
the depth of nodes 7 and 4 is 3.


Example 2:

Input: node = [1]
Output: [1]
Explanation: The node is the deepest node in the tree, and it's the lca of itself.

Example 3:

Input: node = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.
 

Constraints:

The number of nodes in the tree will be in the range [1, 1000].
0 <= Node.val <= 1000
The values of the nodes in the tree are unique.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def lcaDeepestLeaves(self, root):
        self.lca = None
        self.depth = 0
            
        def height(node, depth):
            self.depth = max(self.depth, depth) 
            if node == None:
                return depth
            
            left = height(node.left, depth + 1)
            right = height(node.right, depth + 1)
            
            if left == right == self.depth:
                self.lca = node
            
            return max(left, right)
        
        height(root, 0)
        return self.lca


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

sol = Solution()
print(sol.lcaDeepestLeaves(root)) 

