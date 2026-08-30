class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
            or board[r][c] != "O"):
                return 
            board[r][c] = "T"
            capture(r + 1, c) 
            capture(r - 1, c) 
            capture(r, c + 1) 
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and r == 0 or r == ROWS -1 or c == 0 or c == COLS-1):
                    capture(r, c)


        #2. Capture surrounded regions (0 --> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #3. Uncapture unsurrounded regions (T -> 0)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        

        