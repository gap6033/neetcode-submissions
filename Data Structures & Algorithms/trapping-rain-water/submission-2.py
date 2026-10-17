class Solution:
    def trap(self, height: List[int]) -> int:
        right_greater = [0] * len(height)
        max_greater = 0
        for i in range(len(height) - 1, -1, -1):
            if max_greater < height[i]:
                right_greater[i] = 0
                max_greater = height[i]
            else:
                right_greater[i] = max_greater
        
        left_greater = 0
        water_on_top = 0
        for i in range(len(height)):
            curr_greater = min(right_greater[i], left_greater)
            if curr_greater > height[i]:
                water_on_top += curr_greater - height[i]
            left_greater = max(left_greater, height[i])
        return water_on_top
