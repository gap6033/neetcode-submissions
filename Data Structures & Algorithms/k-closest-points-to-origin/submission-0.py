import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            heapq.heappush(max_heap, (-1 * ((x**2 + y**2) ** 0.5), i))

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        for i in range(len(max_heap)):
            _, index = max_heap[i]
            max_heap[i] = points[index]
        return max_heap
        