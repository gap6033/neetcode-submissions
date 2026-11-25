class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_pattern = []
        start = 0
        output = []
        self.dfs(curr_pattern, start, nums, output)
        return output

    def dfs(self, curr_pattern, start, nums, output):
        if start == len(nums):
            output.append(curr_pattern)
            return
        self.dfs(curr_pattern, start + 1, nums, output)
        new_pattern = curr_pattern.copy()
        new_pattern.append(nums[start])
        self.dfs(new_pattern, start + 1, nums, output)
        