class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numMap = {}

        for n in nums:
            numMap[n] = 1 + numMap.get(n, 0)
        
        for key in numMap.keys():
            if numMap[key] == 1:
                return key
        