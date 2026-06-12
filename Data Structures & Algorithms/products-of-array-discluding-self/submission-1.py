class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            cur = 1
            for j in range(len(nums)):
                if j != i:
                    cur *= nums[j]
            res.append(cur)
        
        return res