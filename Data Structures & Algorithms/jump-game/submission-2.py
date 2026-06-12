class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 0:
            return False

        found = False
        
        def dfs(current_index, n):
            nonlocal found

            # children = i + jump size
            # If i am at index i, and nums[i] = k
            # I can move to i + 1, i + 2, ... , t + k
            if current_index == n - 1:
                found = True
                return
            
            if current_index > n - 1:
                return
            
            if nums[current_index] == 0:
                return

            # Children: i + 1 ... i + nums[i]
            jump = 1
            while jump <= nums[current_index]:
                dfs(current_index + jump, n)
                jump += 1
        
        dfs(0, n)
        return found