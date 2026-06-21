class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        index_t = 0
        for i in range(len(s)):
            if s[i] == t[index_t]:
                index_t += 1
            if index_t == len(t):
                break

        return len(t) - index_t