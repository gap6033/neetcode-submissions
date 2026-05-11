class Solution:
    def __init__(self):
        self.output = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.helper(nums, 0, [])
        return self.output


    def helper(self, nums, curr_index, curr_seq):
        if curr_index == len(nums):
            self.output.append(curr_seq.copy())
            return
        curr_num = nums[curr_index]
        curr_seq.append(curr_num)
        self.helper(nums, curr_index + 1, curr_seq)
        curr_seq.pop()
        while curr_index < len(nums) and curr_num == nums[curr_index]:
            curr_index += 1
        self.helper(nums, curr_index, curr_seq)

        
