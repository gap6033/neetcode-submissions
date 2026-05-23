class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        curr_word = ''
        dp = {}
        wordDict = set(wordDict)
        for i in range(len(s)):
            curr_word += s[i]
            if curr_word in wordDict:
                if self.dfs(i + 1, s, wordDict, dp):
                    return True
    
        return False

    def dfs(self, start, s, wordDict, dp):
        if start in dp:
            return dp[start]
        if start == len(s):
            return True
        curr_word = ''
        for i in range(start, len(s)):
            curr_word += s[i]
            if curr_word in wordDict:
                if self.dfs(i + 1, s, wordDict, dp):
                    dp[start] = True
                    return True
        dp[start] = False
        return False
        
