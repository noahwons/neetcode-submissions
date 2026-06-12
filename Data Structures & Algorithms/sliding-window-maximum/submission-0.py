class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # make sure smaller values exist
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # remove left value from window
            if l > q[0]:
                q.popleft()
            
            # make sure input is of size k
            if (r + 1) >= k:
                # append maximum after each iteration
                output.append(nums[q[0]])
                l += 1

            r += 1
        return output