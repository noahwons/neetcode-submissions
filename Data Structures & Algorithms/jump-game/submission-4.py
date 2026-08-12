class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for n in nums]
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            tmp = nums[i]
            while tmp > 0:
                if (i + tmp) in range(len(nums)) and dp[i + tmp]:
                    dp[i] = True
                tmp -= 1
        print(dp)
        return dp[0]