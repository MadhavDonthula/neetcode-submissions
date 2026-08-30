class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r, c): 
            q = collections.deque()
            q.append((r, c))
            visit.add((r,c))
            length = 0 
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while q: 
                row, col = q.popleft()
                length += 1
                for dr, dc in directions: 
                    cr, cc = row+dr, col+dc
                    if cr < 0 or cc < 0 or cr == rows or cc == cols or (cr, cc) in visit or grid[cr][cc] == 0:
                        continue 
                    q.append((cr, cc))
                    visit.add((cr, cc))
            return length
        if not grid: 
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set() 
        res = 0 
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == 1: 
                    lengthfound = bfs(r, c)
                    res = max(res, lengthfound)
        return res

