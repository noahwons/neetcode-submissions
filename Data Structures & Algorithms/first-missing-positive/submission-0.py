class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            seen.add(n)
        
        res = 1
        while res in seen:
            res += 1
        
        return res