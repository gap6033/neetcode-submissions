import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_largest = nums
        heapq.heapify(self.k_largest)
        while len(self.k_largest) > k:
            heapq.heappop(self.k_largest)

    def add(self, val: int) -> int:
        heapq.heappush(self.k_largest, val)
        if len(self.k_largest) > self.k:
            heapq.heappop(self.k_largest)
        kth_element = heapq.heappop(self.k_largest)
        heapq.heappush(self.k_largest, kth_element)
        return kth_element



