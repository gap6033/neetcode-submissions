class Solution:
    def trap(self, height: List[int]) -> int:
        left_greater = []
        max_greater = 0
        for i in range(len(height)):
            curr_greater = height[i]
            if max_greater <= curr_greater:
                left_greater.append(0)
            else:
                left_greater.append(max_greater)
            max_greater = max(max_greater, curr_greater)

        right_greater = [0] * len(height)
        max_greater = 0
        for i in range(len(height) - 1, -1, -1):
            curr_greater = height[i]
            if max_greater <= curr_greater:
                right_greater[i] = 0
            else:
                right_greater[i] = max_greater
            max_greater = max(max_greater, curr_greater)
        

        water_at_top = 0
        for i in range(len(height)):
            min_height = min(left_greater[i], right_greater[i])
            if min_height != 0:
                water_at_top += min_height - height[i]
        return water_at_top
            
        
        