class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Pre-process into hashmap
        ROWS, COLS = len(board), len(board[0])

        rowMap = collections.defaultdict(set)
        colMap = collections.defaultdict(set)
        squareMap = [
            [set(), set(), set()],
            [set(), set(), set()],
            [set(), set(), set()]
        ]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != "." and board[r][c] not in rowMap[r] and board[r][c] not in colMap[c] and board[r][c] not in squareMap[r//3][c//3]:
                    rowMap[r].add(board[r][c])
                    colMap[c].add(board[r][c])
                    squareMap[r//3][c//3].add(board[r][c])
                    
                elif board[r][c] != '.':
                    return False
        

        return True