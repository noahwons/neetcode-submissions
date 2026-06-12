class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # O(n) solution, iterate through input arr 2x to produce
        res = []
        count = 0
        while count < 2:
            for i in range(len(nums)):
                res.append(nums[i])
            count += 1
        
        return res