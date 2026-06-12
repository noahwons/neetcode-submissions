class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use hash set to determine dupe
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or # if the current number is inside the current row
                    board[r][c] in cols[c] or # if the current number is inside the current col
                    board[r][c] in squares[(r //3, c//3)]): 
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True        


