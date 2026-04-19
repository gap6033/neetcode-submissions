class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1]
        for i in range(1, len(nums)):
            prev_product = left_products[i - 1]
            left_products.append(prev_product * nums[i - 1])

        curr_product = 1
        for i in range(len(nums) - 2, -1, -1):
            curr_product *= nums[i + 1]
            left_products[i] = left_products[i] * curr_product

        return left_products

'''
[1, 1, 2, 8]

'''