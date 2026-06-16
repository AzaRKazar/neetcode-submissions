class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brutee
        # maximum=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
                
        #         diff=prices[j]-prices[i]
        #         maximum=max(diff,maximum)
        # return maximum
        #optimal
        min_price=10000000000
        max_profit=0
        for price in prices:
            min_price=min(price,min_price)
            profit=price-min_price
            max_profit=max(max_profit,profit)
        return max_profit