class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       curr_index = 0
       curr_pattern = []
       output = []
       i = 0
       curr_sum = 0
       self.dfs(curr_pattern, nums, target, output, i, curr_sum)
       return output

    def dfs(self, pattern, nums, target, output, i, curr_sum):
        if curr_sum == target:
            output.append(pattern)
            return
        if curr_sum > target:
            return
        if i == len(nums):
            return
        new_pattern = pattern.copy()
        self.dfs(pattern, nums, target, output, i + 1, curr_sum)
        new_pattern.append(nums[i])
        self.dfs(new_pattern, nums, target, output, i, curr_sum + nums[i])