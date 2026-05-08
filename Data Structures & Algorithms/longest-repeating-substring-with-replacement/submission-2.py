class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count = {}
        l = 0
        r = 0
        max_count = 0
        while r < len(s):
            if s[r] not in freq_count:
                freq_count[s[r]] = 0
            freq_count[s[r]] += 1
            while r - l + 1 - self.get_max_freq(freq_count) > k:
                freq_count[s[l]] -= 1
                l += 1
            max_count = max(max_count, r - l + 1)
            r += 1
        return max_count
            
    def get_max_freq(self, freq_count):
        max_count = 0
        for char in freq_count:
            if freq_count[char] > max_count:
                max_count = freq_count[char]
        return max_count


"""
XYKXZY
X:1, Y:2

if r - l + 1 <= k:
    r += 1
else:
    find minimum
"""