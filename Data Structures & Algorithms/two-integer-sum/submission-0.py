class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in my_map:
                return [my_map[difference], i]
            else:
                my_map[nums[i]] = i

        return []