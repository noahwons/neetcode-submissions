class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # increment larger of two otherwise both
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            cur = (min(heights[l], heights[r])) * (r - l)
            res = max(res, cur)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return res