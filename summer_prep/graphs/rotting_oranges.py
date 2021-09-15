class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return -1

        queue = []
        freshOranges = 0
        minutes = 0

        row = len(grid)
        column = len(grid[0])
        
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 2: # rotten oranges 
                    queue.append((r, c, 0))
                
                if grid[r][c] == 1: # fresh oranges 
                    freshOranges += 1
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            print(queue)
            r, c, minutes = queue.pop(0)
            
            for dirn in directions:
                ro, col = r + dirn[0], c + dirn[1]  
                if row > ro >= 0 and column > col >= 0 and \
                grid[ro][col] == 1:
                    queue.append((ro, col, minutes+1))
                    grid[ro][col] = 2
                    freshOranges = freshOranges - 1
        
        if freshOranges > 0: # cannot rot all oranges 
            return -1
        
        return minutes

s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))