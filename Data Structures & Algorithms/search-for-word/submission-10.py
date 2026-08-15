class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        # dfs: explores all neigboring cells unless none match
        def dfs(r, c, idx, visit):
            if r not in range(ROWS) or c not in range(COLS) or idx not in range(len(word)) or board[r][c] != word[idx] or (r, c) in visit:
                return False
            
            if idx == len(word) - 1 and board[r][c] == word[-1]:
                print(idx)
                print(r, c)
                return True
            
            if (r, c) not in visit:
                visit.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if dfs(nr, nc, idx + 1, visit):
                        return True
            visit.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True

        return False