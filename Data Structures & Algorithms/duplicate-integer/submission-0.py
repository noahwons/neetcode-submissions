class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for num in nums:
            if num not in my_map:
                my_map[num] = 1
            else:
                my_map[num] += 1
                
            if my_map[num] > 1:
                return True
                

        return False