class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        paths = self.dfs(0, nums, target)
        if paths == float('inf'):
            return 0
        return paths


    def dfs(self, curr_index, nums, target):
        if curr_index == len(nums) and target == 0:
            return 1
        if curr_index == len(nums):
            return 0
   
        path_add = self.dfs(curr_index + 1, nums, target - nums[curr_index])
       
        path_sub = self.dfs(curr_index + 1, nums, target + nums[curr_index])
        
        return path_add + path_sub

        
