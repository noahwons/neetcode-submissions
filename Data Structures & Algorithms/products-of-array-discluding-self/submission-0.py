class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply all elements in nums asside from nums[i]
        # nums = [1, 2, 3, 4]
        res = [1] * (len(nums))
        # [[1],[1],[1],[1]]

        prefix = 1
        for i in range(len(nums)):
            # i = 0 | 1 | 2 | 3 

            res[i] = prefix
            prefix *= nums[i] # 1 | 2 | 6 | 24

            # [[1],[1],[1],[1]] |
            # [[1],[1],[1],[1]] |
            # [[1],[1],[2],[1]] |
            # [[1],[1],[2],[6]] 

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # i = 0 | 1 | 2 | 3 
            
            res[i] *= postfix
            postfix *= nums[i]
        return res


