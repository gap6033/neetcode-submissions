class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = {}
        ans = 0
        for c in s:
            if c not in freq_map:
                freq_map[c] = 0
            freq_map[c] += 1
            if freq_map[c] % 2 == 0:
                ans += 2
        
        for val in freq_map.values():
            if val % 2 != 0:
                ans += 1
                break
        
        return ans