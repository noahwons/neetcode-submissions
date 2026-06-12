class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 # return 0 for empty subarr

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            # compute max we can rob up unit n
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2