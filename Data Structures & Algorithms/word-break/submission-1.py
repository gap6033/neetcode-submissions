class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        curr_word = []
        dp = {}
        wordDict = set(wordDict)
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                if self.dfs(i + 1, s, wordDict, dp):
                    return True
    
        return False

    def dfs(self, start, s, wordDict, dp):
        if start in dp:
            return dp[start]
        if start == len(s):
            return True
        for i in range(start, len(s)):
            if s[start:i + 1] in wordDict:
                if self.dfs(i + 1, s, wordDict, dp):
                    dp[start] = True
                    return True
        dp[start] = False
        return False
        
