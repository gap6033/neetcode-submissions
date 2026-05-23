class Solution:
    def numDecodings(self, s: str) -> int:
        curr_index = 0
        dp = {}
        ans = self.dfs(curr_index, s, dp)
        print(dp)
        return ans


    def dfs(self, curr_index, s, dp):
        if curr_index >= len(s):
            return 1
        if s[curr_index] == "0":
            return 0
        if curr_index in dp:
            return dp[curr_index]
        curr_sum = self.dfs(curr_index + 1, s, dp)
        if curr_index + 1 < len(s) and int(s[curr_index] + s[curr_index + 1]) <= 26:
            curr_sum += self.dfs(curr_index + 2, s, dp)
        dp[curr_index] = curr_sum
        return curr_sum

