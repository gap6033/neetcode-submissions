class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_smaller = self.left_smaller(heights)
        right_smaller = self.right_smaller(heights)
        max_area = 0
        for i in range(len(heights)):
            curr_max = heights[i] * (1 + (i - left_smaller[i]) + (right_smaller[i] - i))
            max_area = max(curr_max, max_area)
        return max_area


    def left_smaller(self, array):
        stack = []
        left_smaller = []
        for i in range(len(array)):
            while stack and array[stack[-1]] >= array[i]:
                stack.pop()
            if not stack:
                left_smaller.append(0)
            else:
                left_smaller.append(stack[-1] + 1)
            stack.append(i)
        return left_smaller

    def right_smaller(self, array):
        stack = []
        right_smaller = []
        for i in range(len(array) - 1, -1, -1):
            while stack and array[stack[-1]] >= array[i]:
                stack.pop()
            if not stack:
                right_smaller.append(len(array) - 1)
            else:
                right_smaller.append(stack[-1] - 1)
            stack.append(i)
        return right_smaller[::-1]


"""
0.  1. 2. 3. 4. 5
[7, 1, 7, 2, 2, 4]

left_smaller = [0, 0, 2, 2, 2, 5]
right_smaller = [0, 5, 2, 5, 5, 5]

a[i] * (1 + (i - l) + (r - i))
7 * (1 + 0-0 + 0 - 0) = 7
1 * (1 + (1 - 0) + (5 - 1)) = 6
7 * (1 + (2 - 2) + (2 - 2)) = 7
2 * (1 + (3 - 2) + (5 - 3)) = 8
2 * (1 + (4 - 2) + (5 - 4)) = 8
"""