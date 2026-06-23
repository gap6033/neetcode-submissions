
class Solution:

    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l = 0
        r = 10**9
        ans = float('inf')
        while l <= r:
            m = l + (r - l)//2
            if self.is_valid(m, nums, p):
                r = m - 1
                ans = min(m, ans)
            else:
                l = m + 1
        return ans

    def is_valid(self, m, nums, p):
        ans = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= m:
                ans += 1
                i += 2
            else:
                i += 1
            if ans == p:
                return True
        return False
