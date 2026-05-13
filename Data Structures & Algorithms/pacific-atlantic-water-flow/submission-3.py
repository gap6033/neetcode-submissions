from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_queue = deque()
        for c in range(len(heights[0])):
            pacific_queue.append([0, c])

        for r in range(1, len(heights)):
            pacific_queue.append([r, 0])

        pacific_set = set()
        
        while pacific_queue:
            r, c = pacific_queue.popleft()
            pacific_set.add((r, c))
            for x, y in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                new_r = r + x
                new_c = c + y
                if self.check_validity(heights[r][c], pacific_set, new_r, new_c, heights):
                    pacific_queue.append((new_r, new_c))

        atlantic_queue = deque()

        for c in range(len(heights[0])):
            atlantic_queue.append([len(heights) - 1, c])

        for r in range(len(heights) - 1):
            atlantic_queue.append([r, len(heights[0]) - 1])

        atlantic_set = set()
        
        while atlantic_queue:
            r, c = atlantic_queue.popleft()
            atlantic_set.add((r, c))
            for x, y in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                new_r = r + x
                new_c = c + y
                if self.check_validity(heights[r][c], atlantic_set, new_r, new_c, heights):
                    atlantic_queue.append((new_r, new_c))
        output = []
        for cell in pacific_set:
            if cell in atlantic_set:
                output.append(list(cell))
        return output

    def check_validity(self, prev_cell, visited, r, c, heights):
        if r < 0 or r == len(heights):
            return False
        if c < 0 or c == len(heights[0]):
            return False
        if (r, c) in visited:
            return False
        if prev_cell > heights[r][c]:
            return False
        return True
