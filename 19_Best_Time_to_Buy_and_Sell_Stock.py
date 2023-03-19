class Solution(object):
    def maxProfit(self, prices):

        if len(prices) < 2:
            return 0
        else:
            minprice = prices[0]
            maxprofit = prices[1] - prices[0]

        for i in range(1, len(prices)):
            currentprice = prices[i]
            currentprofit = prices[i] - minprice
            maxprofit = max(currentprofit, maxprofit)
            minprice = min(currentprice, minprice)
        if maxprofit < 0:
            return 0
        else:
            return maxprofit