class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if self.helper(l + 1, r, s) or self.helper(l, r - 1, s):
                    return True
                return False
            l += 1
            r -= 1
        return True

    def helper(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

'''
cabc
'''