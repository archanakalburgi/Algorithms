'''
542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

class Solution:
    def updateMatrix(self, matrix):
        row = len(matrix) 
        column = len(matrix[0])

        q = []
        for r in range(row):
            for c in range(column):
                if not matrix[r][c]:
                    q.append((r, c))
                else:
                    matrix[r][c] = 999
        while q:
            r, c = q.pop(0) 
            distance = matrix[r][c] + 1
            directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

            for rw, col in directions:
                if 0 <= rw < row and 0 <= col < column and matrix[rw][col] > distance:
                    matrix[rw][col] = distance
                    q.append((rw, col)) 
        return matrix 

matrix = [
 [0,0,0],
 [0,1,0],
 [1,1,1]]

sol = Solution()
print(sol.updateMatrix(matrix))

