class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort input O(nlogn)

        def backtrack(i, subset):
            # base case
            if i == len(nums):
                res.append(subset[::])
                return # return at end of arr

            # recursive case

            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset) # call backtrack on next index
            subset.pop() # remove value we just added

            # all subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1, subset) # ensures empty array is added to result (if while loop skips entire array)
        
        backtrack(0, [])
        return res