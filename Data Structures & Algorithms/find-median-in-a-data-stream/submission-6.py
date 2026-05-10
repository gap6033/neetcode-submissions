

class MedianFinder:

    def __init__(self):
        self.left_side = []
        self.right_side = []

    def addNum(self, num: int) -> None:
        if not self.left_side:
            self.left_side.append(-1 * num)
        else:
            if len(self.left_side) == len(self.right_side):
                popped = heapq.heappop(self.right_side)
            else:
                popped = -1 * heapq.heappop(self.left_side)
            if num > popped:
                heapq.heappush(self.right_side, num)
                heapq.heappush(self.left_side, -1 * popped)
            else:
                heapq.heappush(self.right_side, popped)
                heapq.heappush(self.left_side, -1 * num)

    def findMedian(self) -> float:
        if (len(self.left_side) + len(self.right_side)) % 2 != 0:
            return -1 * self.left_side[0]
        else:
            return (-1 * self.left_side[0] + self.right_side[0])/2



        


'''
[2, 3] [5, 7]
'''