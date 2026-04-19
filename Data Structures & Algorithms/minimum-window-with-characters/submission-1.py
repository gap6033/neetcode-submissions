class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_freq = {}
        for c in t:
            if c not in t_freq:
                t_freq[c] = 0
            t_freq[c] += 1
        
        l = 0
        r = 0
        s_freq = {}
        min_str_len = float('inf')
        min_str = ''
        while r < len(s):
            if s[r] in t_freq:
                if s[r] not in s_freq:
                    s_freq[s[r]] = 0
                s_freq[s[r]] += 1
                if self._check_valid(s_freq, t_freq):
                    while self._check_valid(s_freq, t_freq):
                        curr_min_str = s[l:r+1]
                        if s[l] in s_freq:
                            s_freq[s[l]] -= 1
                            if s_freq[s[l]] == 0:
                                del s_freq[s[l]]
                        l += 1
                    if len(curr_min_str) < min_str_len:
                        min_str_len = len(curr_min_str)
                        min_str = curr_min_str
            r += 1
        return min_str
    
    def _check_valid(self, s_freq, t_freq):
        if len(s_freq) != len(t_freq):
            return False
        for c in t_freq:
            if c not in s_freq:
                return False
            if s_freq[c] >= t_freq[c]:
                continue
            else:
                return False
        return True

