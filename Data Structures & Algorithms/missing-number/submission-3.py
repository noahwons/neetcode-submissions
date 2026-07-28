class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = len(nums) + 1
        # range = 0 ... maxNum

        vals = set()

        for num in nums:
            vals.add(num)
        print(range(maxNum))
        for i in range(maxNum):
            print(i)
            if i not in vals:
                return i
        
