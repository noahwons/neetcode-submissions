class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # use backtracking dfs
        # i is the index of the value we are making a decision on
        subset = [] # use to build each subset
        def dfs(i):
            if i >= len(nums):
                # out of bounds, past leaf node
                res.append(subset.copy())
                return
            
            # decision to include nums[i] (left branch of decision tree)
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res