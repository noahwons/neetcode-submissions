class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        height = float('-inf')

        while l < r:
            height = max(height, (min(heights[l], heights[r])*(r - l)))
            if heights[r] > heights[l]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return height