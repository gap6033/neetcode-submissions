class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = self.build_freq_dict(t, 0, len(t) - 1)
        l = 0
        r = len(t) - 1
        freq_s = self.build_freq_dict(s, 0, r - 1)
        min_len = float('inf')
        while r < len(s):
            if s[r] not in freq_s:
                freq_s[s[r]] = 0
            freq_s[s[r]] += 1
            while self.is_valid(freq_s, freq_t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    indices = [l, r]
                freq_s[s[l]] -= 1
                if freq_s[s[l]] == 0:
                    del freq_s[s[l]]
                l += 1
            r += 1
        if min_len == float('inf'):
            return ""
        return s[indices[0]: indices[1] + 1]
        
            


    def build_freq_dict(self, s, l, r):
        output = {}
        for i in range(l, r + 1):
            if s[i] not in output:
                output[s[i]] = 0
            output[s[i]] += 1
        return output
    
    def is_valid(self, freq_s, freq_t):
        for val in freq_t:
            if val not in freq_s:
                return False
            if freq_s[val] < freq_t[val]:
                return False
        return True

"""
t = XYZ
s = OUZODYXAZV

"""