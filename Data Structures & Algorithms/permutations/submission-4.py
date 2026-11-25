class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        curr_pattern = []
        for i in range(len(nums)):
            curr_pattern.append(nums[0])
            popped = nums.pop(0)
            self.dfs(curr_pattern, nums, output)
            nums.append(popped)
            curr_pattern.pop()
        return output

    def dfs(self, pattern, nums, output):
        if not nums:
            output.append(pattern.copy())
            return
        for i in range(len(nums)):
            pattern.append(nums[0])
            popped = nums.pop(0)
            self.dfs(pattern, nums, output)
            nums.append(popped)
            pattern.pop()
    

'''
[1,2,3]
[2,3]
'''