class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_dict_1 = self.build_freq_dict(s1, 0, len(s1) - 1)
        count_needed = len(freq_dict_1)
        window_size = len(s1)
        l = 0
        r = window_size - 1
        freq_dict_2 = self.build_freq_dict(s2, l, r - 1)
        while r < len(s2):
            # print(freq_dict_2)
            if s2[r] not in freq_dict_2:
                freq_dict_2[s2[r]] = 0
            freq_dict_2[s2[r]] += 1
            if freq_dict_2 == freq_dict_1:
                return True
            freq_dict_2[s2[l]] -= 1
            if freq_dict_2[s2[l]] == 0:
                del freq_dict_2[s2[l]]
            l += 1
            r += 1
        return False
            


    def build_freq_dict(self, s, l, r):
        output = {}
        for i in range(l, r + 1):
            if s[i] not in output:
                output[s[i]] = 0
            output[s[i]] += 1
        return output

"""
a:1, b:1. c:1
c:1, a:1, b:1

"""
