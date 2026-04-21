class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1: 
                return 1
            if (r, c) in visit: 
                return 0 
            visit.add((r, c))
            return (dfs(r+1, c) + dfs(r-1, c) + 
                    dfs(r, c+1) + dfs(r, c-1))
        for i in range(ROWS):
            for y in range(COLS):
                if grid[i][y] == 1:
                    return dfs(i, y)