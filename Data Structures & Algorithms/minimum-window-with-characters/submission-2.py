class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_freq = {}
        for c in t:
            if c not in t_freq:
                t_freq[c] = 0
            t_freq[c] += 1
        need = len(t_freq)
        have = 0
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
                if s_freq[s[r]] == t_freq[s[r]]:
                    have += 1
                if have == need:
                    while have == need:
                        curr_min_str = s[l:r + 1]
                        if s[l] in s_freq:
                            if s_freq[s[l]] == t_freq[s[l]]:
                                have -= 1
                            s_freq[s[l]] -= 1
                            if s_freq[s[l]] == 0:
                                del s_freq[s[l]]
                        l += 1
                    if len(curr_min_str) < min_str_len:
                        min_str_len = len(curr_min_str)
                        min_str = curr_min_str
            r += 1
        return min_str
    
   

