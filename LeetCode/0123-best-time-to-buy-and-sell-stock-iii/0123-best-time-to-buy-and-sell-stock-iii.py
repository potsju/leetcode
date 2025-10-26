class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0 
        minprice = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            profit_today = prices[i] - minprice
            maxprofit = max(maxprofit, profit_today)
            minprice = min(minprice, prices[i])
        return maxprofit