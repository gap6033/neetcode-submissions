class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        prev_target = None
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            target = abs(nums[i])
            if target == prev_target:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                left_num = nums[l]
                right_num = nums[r]
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                    continue
                if total < target:
                    l += 1
                    continue
                if total == target:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == left_num:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == right_num:
                        r -= 1
            prev_target = target
        return output



