class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        last = cols - 1

        r = 0
        while r < rows:
            if target > matrix[r][last]:
                r += 1
            else:
                l, rt = 0, last
                while l <= rt:
                    mid = (l + rt) // 2
                    if target > matrix[r][mid]:
                        l = mid + 1
                    elif target < matrix[r][mid]:
                        rt = mid - 1
                    else:
                        return True
                return False

        return False
