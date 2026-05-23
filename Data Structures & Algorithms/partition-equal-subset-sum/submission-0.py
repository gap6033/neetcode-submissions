class Solution:
    def canPartition(self, coins: List[int]) -> bool:
        total = sum(coins)
        if total % 2 != float(0):
            return False
        amount = int(total/2)
        return self.dfs(0, coins, amount, {})

    def dfs(self, i, coins, amount, dp):
        if (amount, i) in dp:
            return dp[(amount, i)]
        if amount == 0:
            return True
        if i == len(coins):
            return False
        if amount - coins[i] >= 0:
            if self.dfs(i + 1, coins, amount - coins[i], dp):
                dp[(amount, i)] = True
                return True
        if self.dfs(i + 1, coins, amount, dp):
            dp[(amount, i)] = True
            return True
        dp[(amount, i)] = False
        return False