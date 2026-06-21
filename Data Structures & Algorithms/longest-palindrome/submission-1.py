class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = {}
        for c in s:
            if c not in freq_map:
                freq_map[c] = 0
            freq_map[c] += 1
        
        max_odd = 0
        max_odd_char = ''
        even_count = 0
        for c in freq_map:
            if freq_map[c] % 2 == 0:
                even_count += freq_map[c]
            else:
                if freq_map[c] > max_odd:
                    max_odd_char = c
                    max_odd = freq_map[c]

        for c in freq_map:
            if c != max_odd_char and freq_map[c] % 2 != 0:
                even_count += freq_map[c] - 1


        return even_count + max_odd
        