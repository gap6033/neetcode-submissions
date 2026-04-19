class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_buy = float('inf')
        for num in prices:
            if num < curr_buy:
                curr_buy = num
            else:
                max_profit = max(max_profit, num - curr_buy)
        return max_profit