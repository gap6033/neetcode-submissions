class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        index = 0
        output = []
        curr_sum = 0
        nums.sort()
        self.helper(nums, [], index, output, curr_sum, target)
        return output

    def helper(self, nums, curr_set, index, output, curr_sum, target):
        if index == len(nums) or curr_sum > target:
            return
        if curr_sum == target:
            output.append(curr_set.copy())
            return
        if curr_sum < target:
            curr_set.append(nums[index])
            self.helper(nums, curr_set, index, output, curr_sum + nums[index], target)
            curr_set.pop()
            self.helper(nums, curr_set, index + 1, output, curr_sum, target)
