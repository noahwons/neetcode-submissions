class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # center can only be either 1x1 of 2x2
        # if odd, center is at matrix[n//2][n//2]

        ROWS, COLS = len(matrix) - 1, len(matrix[0]) - 1

        # tmp = (0, 0)
        # (0, 0) = (n, 0)
        # (n, 0) = (n, n)
        # (n, n) = (0, n)
        # (0, n) = tmp

        # (0, 1) = (n - 1, 0)
        # (n - 1, 0) = (n, n - 1)
        # ()

        for r in range(len(matrix)-1//2):
            for c in range(r, len(matrix[r:])-1):
                tmp = matrix[r][c]
                print(ROWS - c, c)
                matrix[r][c] = matrix[ROWS - c][r]
                print("matrix[r][c] = " + str(matrix[ROWS - c][r]))
                matrix[ROWS - c][r] = matrix[ROWS - r][COLS - c]
                matrix[ROWS - r][COLS - c] = matrix[c][COLS - r]
                matrix[c][COLS - r] = tmp
        
