class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = {}
        for c in s:
            if c not in freq_map:
                freq_map[c] = 0
            freq_map[c] += 1

        output = 0
        odd_counted = False
        for c in freq_map:
            if freq_map[c] % 2 == 0:
                output += freq_map[c]
            else:
                if not odd_counted:
                    output += freq_map[c]
                    odd_counted = True
                else:
                    output += freq_map[c] - 1
        
        return output