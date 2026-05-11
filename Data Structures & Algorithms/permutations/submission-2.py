class Solution:
    def __init__(self):
        self.output = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        curr_pattern = []
        self.helper(nums, curr_pattern, 0)
        return self.output

    
    def helper(self, nums, curr_pattern, s):
        if len(curr_pattern) == len(nums):
            self.output.append(curr_pattern.copy())
            return
        for i in range(s, len(nums)):
            nums[s], nums[i] = nums[i], nums[s]
            curr_pattern.append(nums[s])
            self.helper(nums, curr_pattern, s + 1)
            curr_pattern.pop()
            nums[s], nums[i] = nums[i], nums[s]

'''
nums = [1,2,3]
curr_pattern = [2], nums = [3,1]
curr_pattern = [1,], nums = [2,3]
curr_pattern = [1,3], nums = [2,]

'''