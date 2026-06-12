class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        
        l, r = 0, 1
        res = [[1]]
        for i in range(1, numRows):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        
        return res