class Solution:
    def twoSum(self, s: List[int], target: int) -> List[int]:
        l = 0
        r = len(s) - 1

        while l < r:
            comb_sum = s[r] + s[l]
            if comb_sum == target:
                return [l + 1, r + 1]
            if comb_sum < target:
                l += 1
            if comb_sum > target:
                r -= 1