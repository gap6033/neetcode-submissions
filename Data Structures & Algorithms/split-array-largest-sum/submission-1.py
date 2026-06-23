class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            m = l + (r - l)//2
            if self.is_valid(m, nums, k):
                r = m - 1
                res = m
            else:
                l = m + 1
        return res


    def is_valid(self, m, nums, k):
        curr_sum = 0
        sub_array_cnt = 0
        for i in range(len(nums)):
            if nums[i] + curr_sum <= m:
                curr_sum += nums[i]
                continue
            else:
                sub_array_cnt += 1
                if sub_array_cnt == k:
                    return False
                curr_sum = nums[i]
                
        return True
