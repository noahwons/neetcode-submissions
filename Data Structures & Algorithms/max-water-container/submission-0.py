class Solution:
    def maxArea(self, heights: List[int]) -> int:
        for i in enumerate(heights):
            # Brute force
            maxArea = -1
            for i in range(len(heights)):
                tmpMax = -1
                cur = -1
                dist = 0
                for j in range(i, len(heights)):
                    if heights[i] > heights[j]:
                        cur = heights[j] * dist
                    else:
                        cur = heights[i] * dist
                    if cur > tmpMax:
                            tmpMax = cur
                    dist += 1
                if tmpMax > maxArea:
                    maxArea = tmpMax
            
            return maxArea