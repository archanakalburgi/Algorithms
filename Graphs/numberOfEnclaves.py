'''
1020. Number of Enclaves

Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, 
or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid 
in any number of moves.

 Example 1:

Input: [
    [0,0,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,0,0,0]
    ]
Output: 3

Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.


Example 2:

Input: [
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,0],
    [0,0,0,0]
    ]
Output: 0

Explanation: 
All 1s are either on the boundary or can reach the boundary. 
 

Note:
1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
'''

'''
- travel across the grid 
- perfrom dfs on all 1's that are on the border 
- make all border 1 = 0 ()
'''

class Solution(object):
    def numEnclaves(self, board):
        self.board = board
        count = 0 
        row = len(board) 
        column = len(board[0]) 
        for r in range(row):
            for c in range(column):
                if board[r][c] == 1 and (r == 0 or r == row-1 or c == 0 or c == column-1):
                    self.dfs(board,r,c)

        for r in range(row):
            for c in range(column):
                if self.board[r][c] == 1:
                    count = count + 1
        
        return count

    def dfs(self, board, r, c):
        if r < 0 or r >= len(self.board) or c < 0 or c >= len(self.board[0]) or self.board[r][c]==0:
            return None
        self.board[r][c] = 0
        self.dfs(board,r+1,c)
        self.dfs(board,r-1,c)
        self.dfs(board,r,c+1)
        self.dfs(board,r,c-1) 
        return None

A = [
    [0,0,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,0,0,0]
    ]       
sol = Solution()
print(sol.numEnclaves(A)) 

'''
print(A)
[
    [0, 0, 0, 0], 
    [0, 0, 1, 0], 
    [0, 1, 1, 0], 
    [0, 0, 0, 0]
]

            surrounding regions             number of enclaves 
o/p :         [[]] (board)                      int (no of land squares)
              modify given board                no need to modify, only count
'''