class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = s[0]
        for i in range(len(s)):
            curr_s = s[i]
            left = i - 1
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_s = s[left] + curr_s + s[right]
                left -= 1
                right += 1
            if len(curr_s) > len(max_str):
                max_str = curr_s

            if i + 1 < len(s) and s[i] == s[i + 1]:
                curr_s = s[i] + s[i + 1]
                left = i - 1
                right = i + 2

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    curr_s = s[left] + curr_s + s[right]
                    left -= 1
                    right += 1
                if len(curr_s) > len(max_str):
                    max_str = curr_s
        return max_str

                
