class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            length = r - l
            height = min(heights[r], heights[l])
            max_area = max(max_area, height * length)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area