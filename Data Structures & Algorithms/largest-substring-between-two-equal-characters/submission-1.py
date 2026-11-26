class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        prev_equal = {}
        max_len = -1
        for i in range(len(s)):
            if s[i] not in prev_equal:
                prev_equal[s[i]] = i
            else:
                curr_max = i - prev_equal[s[i]] - 1
                max_len = max(curr_max, max_len)
        return max_len