class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if i%2 == 0:
                if nums[i] <= nums[i + 1]:
                    continue
                else:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] >= nums[i + 1]:
                    continue
                else:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
'''
[3,5,2,1,6,4]
3,5,1,6,2
next_smaller = [2]
'''  