class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        last_cookie_index = 0
        for i in range(len(g)):
            for j in range(last_cookie_index, len(s)):
                if s[j] >= g[i]:
                    ans += 1
                    last_cookie_index = j + 1
                    break
        return ans


'''
[1,3,1,2]
[1,2,3]
[1,1,2,3]
'''