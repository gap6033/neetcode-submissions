class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        total = 0
        ans = 1
        while r < len(nums):
            if nums[r] * (r - l + 1) <= total + nums[r] + k:
                total += nums[r]
                ans = max(ans, r - l + 1)
                print('total', total, 'r', r, 'l', l)
                r += 1
            else:
                total -= nums[l]
                l += 1
        
        return ans

'''
nums = [1, 4, 8, 13]

'''
     