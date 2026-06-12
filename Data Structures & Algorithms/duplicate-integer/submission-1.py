class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # solution 1
        # sort nums, determine if i == i - 1
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and (nums[i] == nums[i-1]):
                return True
        
        return False