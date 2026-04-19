class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1]
        for i in range(1, len(nums)):
            prev_product = left_products[i - 1]
            left_products.append(prev_product * nums[i - 1])

        right_products = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            prev_product = right_products[i + 1]
            right_products[i] = prev_product * nums[i + 1]

        output = []
        for i in range(len(left_products)):
            output.append(left_products[i] * right_products[i])
        return output

'''
[1, 1, 2, 8]
[1, -1, 0, ]
'''