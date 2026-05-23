class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curr_index = 0
        dp = {}
        path_a = self.helper(curr_index, nums[:-1], dp)
        dp = {}
        path_a = max(path_a, self.helper(curr_index, nums[1:], dp))

        return path_a

    def helper(self, curr_index, nums, dp):
        if curr_index in dp:
            return dp[curr_index]
        if curr_index >= len(nums):
            return 0
        path_a = nums[curr_index] + self.helper(curr_index + 2, nums, dp)
        if curr_index + 1 < len(nums):
            path_a = max(path_a, nums[curr_index + 1] + self.helper(curr_index + 3, nums, dp))
        dp[curr_index] = path_a
        return path_a