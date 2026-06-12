class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:



        return self.oOfNWithDivide(nums)
    
    def oOfNWithDivide(self, nums):
        res = []
        total = 1
        numZero = 0

        for n in nums:
            if n != 0:
                total *= n
            else:
                numZero += 1
        
        if numZero == 0:
            for n in nums:
                res.append(total//n)
        elif numZero == 1:
            for n in nums:
                res.append(total if n == 0 else 0)
        else:
            res = [0] * len(nums)
        
        return res
    
    def bruteForce(self, nums):
        res = []

        # O(n^2) solution
        for i in range(len(nums)):
            cur = 1
            for j in range(len(nums)):
                if j != i:
                    cur *= nums[j]
            res.append(cur)
        
        return res