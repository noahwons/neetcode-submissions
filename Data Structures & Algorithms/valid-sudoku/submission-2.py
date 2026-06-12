class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # init empty sets for each row and each col
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        subgrids = defaultdict(set)
        
        # now we have to populate these sets. We can immedietly
        # return false if we find a value that is already in the 
        # set. We also have to skip ".".

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in cols[c]) or (board[r][c] in rows[r]) or (board[r][c] in subgrids[(r // 3, c // 3)]):
                    return False
                else:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    subgrids[(r // 3, c // 3)].add(board[r][c])
        return True

