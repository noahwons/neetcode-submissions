class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, 1

        # brute force find all areas and return max
        
        maxArea = min(heights[l], heights[r]) * (r - l)

        while l < len(heights):
            while r < len(heights):
                curArea = min(heights[l], heights[r]) * (r - l)
                maxArea = max(curArea, maxArea)
                r += 1
            l += 1
            r = l + 1
        
        return maxArea