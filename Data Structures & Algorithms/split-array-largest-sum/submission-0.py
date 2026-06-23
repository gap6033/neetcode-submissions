class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        return self.dfs(0, nums, k, {})

    def dfs(self, curr_index, nums, k, dp):
        if (curr_index, k) in dp:
            return dp[(curr_index, k)]
        if curr_index == len(nums): 
            if k:
                return float('inf')
            else:
                return 0
        if k == 0:
            return float('inf')
        curr_sum = 0
        max_sum = float('inf')
        for i in range(curr_index, len(nums)):
            curr_sum += nums[i]
            max_sum = min(max_sum, max(curr_sum, self.dfs(i + 1, nums, k - 1, dp)))
        dp[(curr_index, k)] = max_sum
        return max_sum

'''

'''