class Solution:
    def lengthOfLongestSubstring(self, strings: str) -> int:
        visited = {}
        l = 0
        r = 0
        max_count = 0
        while r < len(strings):
            if strings[r] not in visited:
                visited[strings[r]] = r
                r += 1
            else:
                max_count = max(max_count, r - l)
                for i in range(l, visited[strings[r]]):
                    del visited[strings[i]]
                l = visited[strings[r]] + 1
                visited[strings[r]] = r
                r += 1
        return max(max_count, r - l)

"""

"""