class DFS:
    def __init__(self):
        self.visited = set()
    
    def valid_neighbors(self, r, c, row, col):
        valid = []
        neighbors = [(r,c+1),(r,c-1),(r-1,c),(r+1,c)]
        for (nr,nc) in neighbors:
            if 0 <= nr < row and 0 <= nc < col: 
                valid.append((nr,nc))
        return valid
    
    def dfs(self, row, col, matrix,traversal):
        self.visited.add((row,col))
        traversal.append(matrix[row][col]) 
        for (nr,nc) in self.valid_neighbors(row, col, len(matrix), len(matrix[0])):
            if (nr,nc) not in self.visited:
                self.dfs(nr,nc,matrix,traversal)
        return traversal 

    def function(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        traversal = []
        for ro in range(row):
            for col in range(column):
                if (ro,col) not in self.visited:
                    return self.dfs(ro,col,matrix, []) 




matrix = [
    ['A','B','C','D'],
    ['E','F','G','H'],
    ['I','J','K','L'],
    ['M','N','O','P']
]
d = DFS()
print(d.function(matrix))
