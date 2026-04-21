class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1 or (r, c) in visit:  
                return 0
            visit.add((r, c))
            return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)
        for ir in range(ROWS):
            for ic in range(COLS):
                if grid[ir][ic] == 1: 
                    currArea = dfs(ir, ic)
                    if currArea > max_area: 
                        max_area = currArea
        return max_area
            

