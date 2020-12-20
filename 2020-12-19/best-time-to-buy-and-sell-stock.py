class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = float('inf')
        profit = 0
        for price in prices:
            if bp > price:
                bp = price
            else:
                if price - bp > profit:
                    profit = price - bp
        return profit
        