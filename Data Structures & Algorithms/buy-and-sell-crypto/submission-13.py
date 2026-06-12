class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = l + 1
        while r < len(prices):
            if prices[l] < prices[r]:
                curProfit = prices[r] - prices[l]
                profit = max(profit, curProfit)
            else:
                l = r
            r += 1
                
            
            
        return profit