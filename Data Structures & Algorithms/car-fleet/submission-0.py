class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(speed)):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort()

        fleet_count = 1
        prev_time = (target - pos_speed[-1][0])/pos_speed[-1][1]
        for i in range(len(pos_speed) - 2, -1, -1):
            curr_time = (target - pos_speed[i][0])/pos_speed[i][1]
            if curr_time <= prev_time:
                continue
            else:
                fleet_count += 1
                prev_time = curr_time
        return fleet_count
"""
Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
[(4,2), (1,2), (0,1), (7,1)]
[(0,1), (1,2), (4,2), (7,1)]
10-0//1 = 10
10-1//2 = 4.5
10-4//2 = 3
10-7//1 = 3
"""