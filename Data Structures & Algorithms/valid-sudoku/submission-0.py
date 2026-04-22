class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def checkDuplicates(arr):
            map = {}
            for i in arr: 
                if i != ".":
                    map[i] = map.get(i, 0) + 1
                    if map[i] > 1: 
                        return False
            return True
        for r in range(ROWS):
            if not checkDuplicates(board[r]):
                return False
        for c in range(COLS):
            col = [row[c] for row in board]
            if not checkDuplicates(col): 
                return False
        for br in range(3):
            for bc in range(3):
                square = []
                for r in range(3*br, 3*br + 3):
                    for c in range(3*bc, 3*bc + 3):
                        square.append(board[r][c])
                if not checkDuplicates(square):
                    return False
        
        return True
        
