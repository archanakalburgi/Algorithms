'''
863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

        
            3
        /       \
       5         1
      / \       / \
     6   2     0   8
        / \   
       7   4 


Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

'''

'''
i/p -> 
root 
target -> one of the nodes in the tree 
k -> distance (no of edges between target node and other nodes in the tree) 

o/p -> list 

return all nodes that are k distance(edges) away from target node  
'''

'''
    1
   / \
  2   3

target = starting point   
'''