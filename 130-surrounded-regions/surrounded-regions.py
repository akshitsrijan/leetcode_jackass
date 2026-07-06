class Solution:
    
    def dfs(self, board, r, c):
        
        rows = len(board)
        cols = len(board[0])

        # boundary check
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return

        # stop if not O
        if board[r][c] != 'O':
            return

        # mark as safe
        board[r][c] = '#'

        # explore 4 directions
        self.dfs(board, r + 1, c)
        self.dfs(board, r - 1, c)
        self.dfs(board, r, c + 1)
        self.dfs(board, r, c - 1)

    def solve(self, board):
        
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        # traverse left and right boundaries
        for i in range(rows):

            if board[i][0] == 'O':
                self.dfs(board, i, 0)

            if board[i][cols - 1] == 'O':
                self.dfs(board, i, cols - 1)

        # traverse top and bottom boundaries
        for j in range(cols):

            if board[0][j] == 'O':
                self.dfs(board, 0, j)

            if board[rows - 1][j] == 'O':
                self.dfs(board, rows - 1, j)

        # convert surrounded O -> X
        # restore safe # -> O
        for i in range(rows):
            for j in range(cols):

                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == '#':
                    board[i][j] = 'O'