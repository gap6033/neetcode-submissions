class Solution:
    def __init__(self):
        self.output = []
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_set = []
        index = 0
        self.dfs(nums, index + 1, [nums[index]])
        self.dfs(nums, index + 1, [])
        return self.output


    def dfs(self, nums, index, curr_set):
        if index == len(nums):
            self.output.append(curr_set)
            return
        set_1 = curr_set.copy()
        set_1.append(nums[index])
        self.dfs(nums, index + 1, set_1)
        self.dfs(nums, index + 1, curr_set)