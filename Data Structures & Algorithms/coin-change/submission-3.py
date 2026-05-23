class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = self.dfs(0, coins, amount, {})
        if count == float('inf'):
            return -1
        return count
    


    def dfs(self, i, coins, amount, dp):
        if (amount, i) in dp:
            return dp[(amount, i)]
        if amount == 0:
            return 0
        if i == len(coins) and amount != 0:
            return float('inf')
        count = float('inf')
        if amount - coins[i] >= 0:
            count = 1 + self.dfs(i, coins, amount - coins[i], dp)
        count = min(count, self.dfs(i + 1, coins, amount, dp))
        dp[(amount, i)] = count
        return count