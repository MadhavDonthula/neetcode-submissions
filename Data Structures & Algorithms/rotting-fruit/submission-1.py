from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        operations = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minutes = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
        while queue:
            currLen = len(queue)
            added = False
            for i in range(currLen):
                r, c = queue.popleft()
                for dr, dc in operations:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        added = True
            if added:
                minutes += 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return minutes