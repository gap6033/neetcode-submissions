import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -1 * stone)

        while len(max_heap) > 1:
            stone_1 = -1 * heapq.heappop(max_heap)
            stone_2 = -1 * heapq.heappop(max_heap)
            diff = stone_1 - stone_2
            if diff > 0:
                heapq.heappush(max_heap, -1 * diff)
            
        if max_heap:
            return -1 * max_heap[0]
        return 0