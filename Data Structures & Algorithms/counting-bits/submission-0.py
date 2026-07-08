class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 -> 0 = 0
        # 1 -> 1 = 1
        # 2 -> 10 = 1
        # 3 -> 11 = 2
        # 4 -> 100 = 1
        # Bin = [..., 128, 64, 32, 16, 8, 4, 2, 1, 0]
        #     = [..., 2^7, 2^6, 2^5, 2^4, 2^3, 2^2, 2^1, 2^0]

        res = []
        for i in range(n+1):
            res.append(self.convertToBinary(i))

        return res

    
    def convertToBinary(self, num):
        """ Given integer num, convert to binary """
        tmp = num
        ones = 0
        while tmp > 0:
            if tmp % 2 == 1:
                ones += 1
            tmp //= 2
        return ones

