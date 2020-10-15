'''
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which 
the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''

'''
in bst -> 
    left < right
    root > left
    root < right 

binary tree construction :
    binary search : returns mid (middle element of array)
    make mid = root 

[-10, -9, 0, 5, 9]

i/p                                 o/p                     how
func(nums, start, len(nums)->end) -> 0                  nums = [-10,-9,0,5,9]
func(nums, start, mid)            ->                    nums = [-10,-9]
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructTree(self, nums, start, end): # ([-10, -3, 0, 5, 9], 0, 4) | ([-10, -3, 0, 5, 9], 0, 1) | ([-10, -3, 0, 5, 9], 0, -1)| ([-10, -3, 0, 5, 9],3,4)| ([-10, -3 0, 5, 9],4,4)
        if start > end:      # 0 > 4 -> F | 0 > 1 -> F | 0 > -1 -> T | 0 > 1 | 1 > 1 | 1 > 0 | 1 > 1 | 2 > 1 | 1 > 1 | 3 > 4 | 3 > 2 | 4 > 4 | 4 > 3 | 5 > 4    
            return 
        
        else :
            mid = (start + end) // 2  # mid = 2 | mid = 0 | mid = 0 | mid = 1 | mid = 1 | mid = 3 | mid = 4
             
            root = TreeNode(nums[mid]) # root = TreeNode(0) | root = TreeNode(-10) | -3 | 5 | 9
            root.left = self.constructTree(nums, start, mid-1) # root.left = construct([-10,-3,0,5,9], 0, 1) | root.left = construct([-10, -3, 0, 5, 9], 0, -1) 
            root.right = self.constructTree(nums, mid+1, end)  # root.right = construct([-10, -3, 0, 5, 9], 3, 4) | root.right = construct([-10, -3, 0, 5, 9], 4, 4)| 
            return root 

    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return 
        else :
            return self.constructTree(nums, 0, len(nums)-1) 

sol = Solution()
node = sol.sortedArrayToBST([-10,-3,0,5,9])
print(node)
print(node.left)
print(node.right)

        

      