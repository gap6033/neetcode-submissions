class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map_s = [0] * 26
        for i in range(len(s)):
            char_map_s[ord(s[i]) - ord('a')] += 1

        char_map_t = [0] * 26
        for i in range(len(t)):
            char_map_t[ord(t[i]) - ord('a')] += 1
        
        if char_map_s == char_map_t:
            return True
        return False
"""
sort = s log s + t log t + s + t



"""