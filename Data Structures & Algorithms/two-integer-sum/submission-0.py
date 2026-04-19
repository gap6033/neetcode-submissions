class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in visited:
                return [visited[target - num], i]
            visited[num] = i
