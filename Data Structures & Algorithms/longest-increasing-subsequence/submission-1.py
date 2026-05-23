class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        curr_index = 0
        prev = float('-inf')
        max_len = 1
        dp = {}
        if nums[curr_index] > prev:
            max_len = 1 + self.dfs(curr_index + 1, nums, nums[curr_index], dp)
        max_len = max(max_len, self.dfs(curr_index + 1, nums, prev, dp))
        return max_len

    def dfs(self, curr_index, nums, prev, dp):
        if (curr_index, prev) in dp:
            return dp[(curr_index, prev)]
        if curr_index == len(nums):
            return 0
        max_len = 0
        if nums[curr_index] > prev:
            max_len = 1 + self.dfs(curr_index + 1, nums, nums[curr_index], dp)
        max_len = max(max_len, self.dfs(curr_index + 1, nums, prev, dp))
        dp[(curr_index, prev)] = max_len
        return max_len

        