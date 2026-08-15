class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # prevent from re-visiting cells in same path
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != word[i] or (r, c) in path:
                return False
            
            path.add((r, c))
            res = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    res = True
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0): return True
        
        return False

            