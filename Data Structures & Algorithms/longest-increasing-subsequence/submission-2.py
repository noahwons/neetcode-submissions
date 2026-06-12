class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums) # all values have length of 1 (themselves)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]: # must be true for LIS
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS) # O(n^2)