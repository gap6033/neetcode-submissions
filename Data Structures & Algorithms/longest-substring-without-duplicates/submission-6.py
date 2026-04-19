class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in char_set:
                while s[l] != s[r]:
                    char_set.remove(s[l])
                    l += 1
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1

        
        return max_len