'''
1162. As Far from Land as Possible

Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, 
find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: 
the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.


Example 1:

Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.


Example 2:

Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
'''

class Solution:
    def maxDistance(self, grid):
        # put all 1's in queue and do bfs
        if not grid:
            return -1

        queue = []
        row = len(grid) 
        column = len(grid[0])
        visited = set()

        for r in range(row):
            for c in range(column):
                if grid[r][c]:
                    queue.append((r, c, 0)) 
                    visited.add((r, c))
        
        result = -1

        while queue:
            Row, Column, length = queue.pop(0)
            result = max(result, length)
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for dr, dc in directions:
                ro, col = Row + dr, Column + dc
                
                if 0 <= ro < row and 0 <= col < column and (ro, col) not in visited:
                    queue.append((ro, col, length + 1))
                    visited.add((ro, col))
                    
        if result == 0:
            return -1
        return result


sol = Solution()
grid = [[1,0,1],[0,0,0],[1,0,1]]
# grid = [[1,1,1,1]]
# sol.maxDistance(grid)
print(sol.maxDistance(grid)) 
