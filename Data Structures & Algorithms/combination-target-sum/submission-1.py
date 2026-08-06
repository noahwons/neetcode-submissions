class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i not in range(len(nums)) or total > target:
                return
            
            # choose to include nums[i]
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # remove nums[i]
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res