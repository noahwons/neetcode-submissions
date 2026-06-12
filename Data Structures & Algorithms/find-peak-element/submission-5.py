class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # run BS on greater side
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2

            # left neighbor greater
            if mid > 0 and nums[mid] < nums[mid - 1]:
                # we check if mid > 0 b/c if it is 0,
                # it will always be greater then its left neighbor

                # in other words, if mid == 0, nums[mid] > nums[mid - 1]
                # also prevents out of bounds
                r = mid - 1

            # right neighbor greater
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            
            else:
                return mid
        
