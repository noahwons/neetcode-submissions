class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Dimensions
        ROWS, COLS = len(board), len(board[0])

        # cannot revisit, use a set to add current positions
        # we have visited so we do not revisit
        path = set()
        
        # r, c represent current position
        # i represents position in word
        def dfs(r, c, i):
            if i == len(word):
                return True

            # return false if out of bounds
            # return false if we see a character if we are not looking for
            # return false if position in path
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            # We know here that we have found the character we are looking for
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            
            # clean path, position no longer has to be considered
            path.remove((r, c))
            return res
        
        # run dfs on all positions in the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        
        # word was not found
        return False

        # Time complexity: O(n * m * dfs)
        # 4^len(word) since we call 4 times for each word
        # Time complexity: O(n * m * 4^n)
                