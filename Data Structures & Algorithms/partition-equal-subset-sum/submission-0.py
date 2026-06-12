class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum is odd, we cannot partition into
        # equal half
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                # save values from original dp
                nextDP.add(t)
            dp = nextDP
        
        return True if target in dp else False