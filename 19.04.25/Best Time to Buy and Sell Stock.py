class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')  # Start with a very high price
        max_profit = 0

        # Loop through prices
        for price in prices:
            # Update the minimum price if a lower price is found
            if price < min_price:
                min_price = price
            # Calculate potential profit if sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

        
