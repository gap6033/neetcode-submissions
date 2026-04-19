class Solution:
    def trap(self, heights: List[int]) -> int:
        # left_greater = self.get_left_greater(heights)
        right_greater = self.get_right_greater(heights)

        water_on_top = 0
        curr_max = 0
        for i in range(len(heights)):
            water_on_top += max(0, min(curr_max, right_greater[i]) - heights[i])
            curr_max = max(curr_max, heights[i])
        
        return water_on_top

    
    def get_left_greater(self, heights):
        output = [0]
        max_height = heights[0]
        for i in range(1, len(heights)):
            output.append(max_height)
            max_height = max(max_height, heights[i])
        return output

    def get_right_greater(self, heights):
        output = [0]
        max_height = heights[-1]
        for i in range(len(heights) -2, -1, -1):
            output.append(max_height)
            max_height = max(max_height, heights[i])
        return output[::-1]


'''
0  1 2 3 4 5 6 7 8 9

                0. 1. 2  3  4. 5  6, 7, 8, 3
left_greater =  [0, 0, 2, 2, 3, 3, 3, 3, 3, 3]
right_greater = [3, 3, 3, 3, 3, 3, 3, 3, 1, 0]
curr_height =   [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
water_level =   [0, 0, 2, 0, 2, 3, 2, 0, 0, 0]

'''
        