class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force Sol
        maxProfit = 0
        for i in range(len(prices)):
            curProfit = 0
            for j in range(i + 1, len(prices)):
                curProfit = max(curProfit, (prices[j] - prices[i]))
            maxProfit = max(maxProfit, curProfit)

        return maxProfit