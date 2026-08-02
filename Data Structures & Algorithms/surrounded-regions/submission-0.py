class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        def bfs(r, c): 
            q = collections.deque()
            q.append([r,c])
            board[r][c] = "T"
            while q:
                row, col = q.popleft()
                for dr, dc in directions: 
                    nr, nc = row+dr, col+dc
                    if (nr < 0 or nc < 0 or nr == rows or nc == cols or board[nr][nc] == "T" or board[nr][nc] == "X"):
                        continue 
                    board[nr][nc] = "T"
                    q.append((nr, nc))
    
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and (r == rows - 1 or c == cols -1 or r == 0 or c == 0)):
                    bfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T": 
                    board[r][c] = "O"
        





