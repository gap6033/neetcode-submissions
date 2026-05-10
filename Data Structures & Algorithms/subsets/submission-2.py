class Solution:
    def __init__(self):
        self.output = []
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        index = 0
        self.dfs(nums, index + 1, [nums[index]])
        self.dfs(nums, index + 1, [])
        return self.output


    def dfs(self, nums, index, curr_set):
        if index == len(nums):
            self.output.append(curr_set.copy())
            return
        curr_set.append(nums[index])
        self.dfs(nums, index + 1, curr_set)
        curr_set.pop()
        self.dfs(nums, index + 1, curr_set)