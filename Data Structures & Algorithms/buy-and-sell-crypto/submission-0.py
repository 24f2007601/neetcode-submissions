from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Track the lowest price seen so far (best day to buy)
        min_price = float('inf')
        # Track the best profit found so far
        max_profit = 0 

        for price in prices:
            if price < min_price:
                # Found a new cheapest buy day — update running minimum
                min_price = price
            elif price - min_price > max_profit:
                # Selling today gives a better profit than anything seen before
                max_profit = price - min_price 

        return max_profit 