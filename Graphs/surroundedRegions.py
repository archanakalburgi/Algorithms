'''
130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board 
are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' 
on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
''' 
'''
** 1 node -> connected to 4 nodes 
1. change all border 0's to $
2. traverse matrix 
3. change 0 -> X
4. change $ -> 0
'''
class Solution(object):
    def solve(self, board):
        self.board = board 
        # print(board)

        row = len(board) 
        if row <= 1: # base case 
            return None

        column = len(board[0]) 
        if column <= 1: # base case 
            return None

        for r in range(row):
            for c in range(column):
                if board[r][c] == 'O' and (r == 0 or r == row-1 or c == 0 or c == column-1):
                    # (border is 0) and (1st or last row) or (1st or last column) -> call dfs
                    self.dfs(r,c) 

        # change the symbols 
        for r in range(row):
            for c in range(column):
                if self.board[r][c] == 'O':
                    self.board[r][c] = 'X'
                if self.board[r][c] == '$': 
                    self.board[r][c] = 'O'        
        # print(self.board)

    def dfs(self, r, c):
        # call dfs on all 4 side of 0's to change the border 0's to $
        if r >= 0 and r < len(self.board) and c >= 0 and c < len(self.board[0]) and self.board[r][c] == 'O':
            # mark 0's on border with '*' 
            self.board[r][c] = '$'
            # call dfs on the neighbouring nodes of '0' 
            self.dfs(r+1,c)
            self.dfs(r-1,c)
            self.dfs(r,c+1)
            self.dfs(r,c-1) 
      
    
board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
        ]   
sol = Solution()
sol.solve(board)
print(board) 


'''
where took time : understanding how is it a graph problem?
made mistake while giving input 
'''

# complexity = no of rows * no of columns 