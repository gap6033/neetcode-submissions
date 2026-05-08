class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_count_s1 = {}
        for i in range(len(s1)):
            if s1[i] not in freq_count_s1:
                freq_count_s1[s1[i]] = 0
            freq_count_s1[s1[i]] += 1

        l = 0
        r = 0
        freq_count_s2 = {}
        while r < len(s2):
            if s2[r] not in freq_count_s2:
                freq_count_s2[s2[r]] = 0
            freq_count_s2[s2[r]] += 1
            if r - l + 1 == len(s1):
                if freq_count_s1 == freq_count_s2:
                    return True
                else:
                    freq_count_s2[s2[l]] -= 1
                    if freq_count_s2[s2[l]] == 0:
                        del freq_count_s2[s2[l]]
                    l += 1
            r += 1               
        return False
                




'''
abc
lecabee

a:1, b:1, c:1
'''