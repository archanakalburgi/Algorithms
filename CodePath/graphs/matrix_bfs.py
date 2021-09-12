class BFS:
    def __init__(self):
        self.visited = set()
    
    def valid_neighbors(self, r, c, row, col):
        valid = []
        neighbors = [(r,c+1),(r,c-1),(r-1,c),(r+1,c)]
        for (nr,nc) in neighbors:
            if 0<=nr<row and 0<=nc<col:
                valid.append((nr,nc))
        return valid

    def bfs(self, row, col, grid):
        q = [(row, col)]
        self.visited.add((row, col))
        traversal =[]
        while q:
            r,c = q.pop(0)
            traversal.append(grid[r][c]) 
            for ((nr, nc)) in self.valid_neighbors(r, c, len(grid), len(grid[0])):
                if ((nr, nc)) not in self.visited:
                    q.append((nr, nc))
                    self.visited.add((nr, nc))
        return traversal 

    def function(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        for r in range(row):
            for c in range(column):
                if (r,c) not in self.visited:
                    print(self.bfs(r,c,matrix))

matrix = [
    ['A','B','C','D'],
    ['E','F','G','H'],
    ['I','J','K','L'],
    ['M','N','O','P']
]
b = BFS()
b.function(matrix)