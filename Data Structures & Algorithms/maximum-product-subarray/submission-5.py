class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        # nums = [-4, -3]
        # i = 0 |
        for i in range(len(nums)):
            cur = nums[i] # cur = nums[0] = -4 |
            maxProd = max(maxProd, cur)
            # j = 1 |
            for j in range(i + 1, len(nums)):
                cur *= nums[j] # cur *= nums[1] = -4 *= -3 = 12|
                maxProd = max(maxProd, cur) # maxProd = max(-4, 12) = 12
                
        
        return maxProd