class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1 

        row = len(grid)
        column = len(grid[0])
        queue = []
        distance = -1
        visited = set() 

        for r in range(row):
            for c in range(column):
                if grid[r][c]:
                    queue.append((r,c,0))
                    visited.add((r,c))
        
        direction = [(-1,0),(1,0),(0,1),(0,-1)] 

        while queue:
            Row, Column, Length = queue.pop(0)
            distance = max(distance, Length)

            for rr, cc in direction: # go through direction list using for loop to go all 4 direction 
                ro = rr + Row
                col = cc + Column

                if 0 <= ro < row and 0 <= col < column and (ro, col) not in visited: # go inside matrix 
                    queue.append((ro, col, Length+1)) 
                    visited.add((ro, col)) 

        if distance == 0:
            return -1 

        return distance 

grid = [[0,0,1]]
sol = Solution() 
print(sol.maxDistance(grid))
