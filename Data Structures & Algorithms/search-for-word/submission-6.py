class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # I feel like we can just run dfs on the first char we find in
        # the grid then return true if we can find the whole word else
        # keep looking
        # return false if non found

        found = False
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i, visit):
            nonlocal found
            if r not in range(ROWS) or c not in range(COLS) or i > len(word) or word[i] != board[r][c]:
                return
            
            if word[i] == board[r][c] and i == len(word) - 1:
                found = True
                return 
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visit:
                    visit.add((nr, nc))
                    dfs(nr, nc, i + 1, visit)
                    visit.remove((nr, nc))
            
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                visit = set({(r, c)})
                if board[r][c] == word[0]:
                    dfs(r, c, 0, visit)
        
        return found