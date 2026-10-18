class Solution:
    def findMin(self, nums: List[int]) -> int:
        return nums[self.find_pivot(nums)]
        
    def find_pivot(self, nums):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l)//2
            if m == len(nums) - 1:
                return m
            elif m == 0:
                if nums[m] < nums[m + 1]:
                    return m
            if nums[m - 1] > nums[m] and nums[m] < nums[m + 1]:
                return m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return m


'''
[4,5,6,0,1,2,3]
[1,2,3,4,5,6]
[2,3,4,5,6,1]
[6,1,2,3,4,5]
[2,1]
'''