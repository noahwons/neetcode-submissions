class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # store x ^ result
        for n in nums:
            res = n ^ res
        return res