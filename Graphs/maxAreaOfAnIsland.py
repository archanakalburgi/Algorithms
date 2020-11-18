'''
695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. 
Note the answer is not 11, because the island must be connected 4-directionally.


Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
'''

class Solution(object):
    def outOfBorder(self, row, column, grid):
        if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]):
           return True

    def maxAreaOfIsland(self, grid):
        area = 0
        self.numOfOnes = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    self.dfs(grid, row, column)
                    area = max(area, self.numOfOnes) 
                    self.numOfOnes = 0
        return area
        
    def dfs(self, grid , row, column):
        # if self.outOfBorder(row,column,grid) or grid[row][column] == 0 or grid[row][column] == 2:
        if self.outOfBorder(row,column,grid) or grid[row][column] == 0:
            return 0
        
        grid[row][column] = 0
        # grid[row][column] = 2
        self.numOfOnes += 1
        self.dfs(grid, row+1, column)
        self.dfs(grid, row-1, column)
        self.dfs(grid, row, column+1)
        self.dfs(grid, row, column-1)
        return self.numOfOnes 

# grid = [[1,1,1,0,0],
#     [1,0,0,0,0],
#     [0,0,0,1,1],
#     [0,0,0,1,0],
#     ]

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

sol = Solution()
print(sol.maxAreaOfIsland(grid)) 

# print(grid)