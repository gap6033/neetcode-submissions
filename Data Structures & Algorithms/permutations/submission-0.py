class Solution:
    def __init__(self):
        self.output = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        curr_pattern = []
        self.helper(nums, curr_pattern)
        return self.output

    
    def helper(self, nums, curr_pattern):
        if len(nums) == 0:
            self.output.append(curr_pattern.copy())
            return
        for num in nums:
            popped = nums.pop(0)
            curr_pattern.append(popped)
            self.helper(nums, curr_pattern)
            nums.append(popped)
            curr_pattern.pop()

'''
nums = [1,2,3]
curr_pattern = [2], nums = [3,1]
curr_pattern = [1,], nums = [2,3]
curr_pattern = [1,3], nums = [2,]

'''