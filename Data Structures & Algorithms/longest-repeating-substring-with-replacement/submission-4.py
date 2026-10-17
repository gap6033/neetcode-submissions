class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dic = {}
        
        l = 0
        r = 0
        max_len = 1
        while r < len(s):
            if s[r] not in freq_dic:
                freq_dic[s[r]] = 0
            freq_dic[s[r]] += 1
            max_count = self.find_max_char(freq_dic)
            while r - l + 1 - max_count > k:
                freq_dic[s[l]] -= 1
                if freq_dic[s[l]] == 0:
                    del freq_dic[s[l]]
                l += 1
                max_count = self.find_max_char(freq_dic)
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len



    def find_max_char(self, freq_dic):
        max_count = 0
        for c in freq_dic:
            max_count = max(max_count, freq_dic[c])
        return max_count
'''
X:1
Y:

r - l + 1 - max_char <= k
'''