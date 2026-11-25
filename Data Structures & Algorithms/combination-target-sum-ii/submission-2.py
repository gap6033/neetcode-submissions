class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        curr_pattern = []
        output = []
        nums.sort()
        self.dfs(curr_pattern, output, nums, target, 0)
        return output

    def dfs(self, pattern, output, nums, target, index):
        if target == 0:
            output.append(pattern)
            return
        if target < 0:
            return
        if index == len(nums):
            return
        new_pattern = pattern.copy()
        curr_num = nums[index]
        new_index = index + 1
        while new_index < len(nums) and nums[new_index] == curr_num:
            new_index += 1
        self.dfs(pattern, output, nums, target, new_index)
        new_pattern.append(nums[index])
        target -= nums[index]
        self.dfs(new_pattern, output, nums, target, index + 1)

