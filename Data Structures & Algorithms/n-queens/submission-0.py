class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 3 sets to retain all required info
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        res = []
        board = [["."] * n for i in range(n)] # create board

        def backtrack(r):
            if r == n:
                # a valid solution has been found

                # add current board to result
                # creats copy of board where the rows are joined to create
                # single string
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue # cannot use this position
                
                # if we can use this solution:

                # update sets
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board [r][c] = "Q"

                # backtrack call
                backtrack(r + 1)

                # Undo (Backtrack frow what we just did to find multiple solutions)
                # we originally set this space to a queen but to find alternative
                # solutions we will set it to an empty space
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board [r][c] = "."
        
        backtrack(0)
        return res