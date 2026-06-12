class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            half = int((l + r) / 2)
            if nums[half] == target:
                return half
            elif nums[half] < target:
                l = half + 1
            elif nums[half] > target:
                r = half - 1


        return -1
