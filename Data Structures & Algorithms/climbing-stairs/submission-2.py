class Solution:
    def climbStairs(self, n: int) -> int:

        res = []
        def backtrack(i):
            if i == n:
                res.append(1)
                return
            
            if i > n:
                return
            
            backtrack(i + 1)
            backtrack(i + 2)

        backtrack(0)
        return len(res)