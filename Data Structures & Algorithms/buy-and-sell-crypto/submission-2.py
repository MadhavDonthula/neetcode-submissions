class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 
        R = 1 
        res = 0
        while L < R and L < len(prices) and R < len(prices): 
            if prices[L] >= prices[R]:
                L = R
                R+=1
            else: 
                profit = prices[R] - prices[L]
                if profit > res: 
                    res = profit
                R+=1
        return res