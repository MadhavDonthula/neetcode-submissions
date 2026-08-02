class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        min = 0 
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = collections.deque()
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == 2: 
                    q.append((r,c))
        
        while q:
            layer = len(q)
            changed = False
            for x in range(layer): 

                row, col = q.popleft()
                for dr, dc in directions: 
                    nr = dr + row
                    nc = dc + col 
                    if (nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] == 2 or grid[nr][nc] == 0): 
                        continue
                    grid[nr][nc] = 2
                    changed = True
                    q.append((nr,nc))
            if changed: 
                min +=1 
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == 1: 
                    return -1
        return min


                    
