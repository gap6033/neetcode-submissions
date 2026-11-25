class Solution:
    

    def partition(self, s: str) -> List[List[str]]:
        output =[]
        curr_pattern = []
        self.dfs(0, s, curr_pattern, output)
        return output

    def dfs(self, curr_index, s, curr_pattern, output):
        if curr_index == len(s):
            output.append(curr_pattern.copy())
            return
        curr_s = ''
        for i in range(curr_index, len(s)):
            curr_s += s[i]
            if self.is_palindrome(curr_s):
                curr_pattern.append(curr_s)
                self.dfs(i + 1, s, curr_pattern, output)
                curr_pattern.pop()

    def is_palindrome(self, pattern):
        l = 0
        r = len(pattern) - 1
        while l < r:
            if pattern[l] != pattern[r]:
                return False
            l += 1
            r -= 1
        return True

'''
dfs called n times
loop in each dfs n, n - 1, n - 2, n - 3...0
n^2
'''