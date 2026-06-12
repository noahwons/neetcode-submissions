class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], [] # quad maintains current quadruplet

        def kSum(k, start, target):
            # NOTE: target changes with each call
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    # len(nums) - k + 1
                    # ignore the last k vals so that there are
                    # at least k vals after so a result of size k
                    # can be calculated and was not ignored
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            # base case, 2sum2
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        kSum(4, 0, target)
        return res