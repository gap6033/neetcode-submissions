class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')
        curr_product = 1
        for i in range(len(nums) - 1, -1, -1):
            max_product = max(curr_product * nums[i], max_product)
            if nums[i] == 0:
                curr_product = 1
            else:
                curr_product *= nums[i]

        curr_product = 1
        for num in nums:
            max_product = max(curr_product * num, max_product)
            if num == 0:
                curr_product = 1
            else:
                curr_product *= num
        
        return max_product

        