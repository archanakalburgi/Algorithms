'''
1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear lengthOfPath from top-left to bottom-right has length k if and only if it is 
composed of cells C_1, C_2, ..., C_k 

such that:
    Adjacent cells C_i and C_{row+1} are connected 8-directionally 
    (ie., they are different and share an edge or corner)

    C_1 is at location (0, 0) (ie. has value grid[0][0])

    C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])

    If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear lengthOfPath from top-left to bottom-right.  
If such a lengthOfPath does not exist, return -1.

Example 1:
Input: [[0,1],[1,0]]
Output: 2

Example 2:
Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1

'''

# class Solution(object):
#     def shortestPathBinaryMatrix(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """

#         row = len(grid)
#         column = len(grid[0])
#         visited = set()
#         queue = []
#         direction = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]  

#         for r in range(row):
#             for c in range(column):
#                 queue.append((r,c))
#                 visited.add((r,c))
#         # print(queue)

#         while len(queue):
#             Row , Column = queue.pop(0)

#             if Row == row-1 and Column == column-1:

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):

        if grid[0][0] == 1:
            return -1
        
        queue = []
        queue.append([0, 0, 0]) 
        visited = set()
        
        while queue:
            row, column, lengthOfPath = queue.pop(0) 
            
            if (row , column) == (len(grid) - 1, len(grid) - 1):
                return lengthOfPath + 1
            
            directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
            
            for dirn in directions:
                r = row + dirn[0]
                c = column + dirn[1] 
                
                if 0 <= r < len(grid) and 0 <= c < len(grid) and (r, c) not in visited and grid[r][c] == 0:
                    queue.append((r, c, lengthOfPath + 1))
                    visited.add((r, c))
                    
        return -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
sol = Solution()
print(sol.shortestPathBinaryMatrix(grid))