class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.res = 1
        memo = {}
        def dfs(num):
            if num == 0:
                return 0
            if num < 0:
                return float('inf')

            if num in memo:
                return memo[num]
            
            res = float('inf')
            for c in coins:
                sub = dfs(num - c)
                res = min(res, sub + 1)
            memo[num] = res
            return res
        sol = dfs(amount)
        return sol if sol < float('inf') else -1
            
            