class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        for i in range(len(nums) + 1):
            sum1 += i
        
        for i in range(len(nums)):
            sum2 += nums[i]
        
        return sum1 - sum2
        
