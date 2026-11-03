class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0
        for num in hashSet:
            if num - 1 not in hashSet:
                length = 1
                while num + length in hashSet:
                    length += 1
                res = max(res, length)
        
        return res
