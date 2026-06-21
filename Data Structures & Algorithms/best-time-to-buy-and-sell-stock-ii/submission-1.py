class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        return self.helper(prices, 0, False, {})

    def helper(self, prices, curr_index, bought, dp):
        if (curr_index, bought) in dp:
            return dp[(curr_index, bought)]
        if curr_index == len(prices):
            return 0
        max_profit = 0
        if bought:
            max_profit = max(max_profit, prices[curr_index] + self.helper(prices, curr_index + 1, False, dp))
            max_profit = max(max_profit, self.helper(prices, curr_index + 1, True, dp))
        else:
            max_profit = max(max_profit, - prices[curr_index] + self.helper(prices, curr_index + 1, True, dp))


        max_profit = max(max_profit, self.helper(prices, curr_index + 1, bought, dp))
        dp[(curr_index, bought)] = max_profit
        return max_profit