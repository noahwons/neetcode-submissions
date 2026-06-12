class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            # update one 
            tmp = one
            one = one + two
            two = tmp
        
        return one
