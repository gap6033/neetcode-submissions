from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dq = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    continue
                dq.append((r, c, 0))

        while dq:
            r, c, curr_distance = dq.popleft()
            if (r, c) in visited:
                continue
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r = r + x
                new_c = c + y
                if new_r < 0 or new_c < 0 or new_r == len(grid) or new_c == len(grid[0]):
                    continue
                if grid[new_r][new_c] in [0, -1]:
                    continue
                if curr_distance + 1 < grid[new_r][new_c]:
                    grid[new_r][new_c] = curr_distance + 1
                    dq.append((new_r, new_c, curr_distance + 1))
            visited.add((r, c))
        return

"""
[
  [2147483647,-1,0,1],
  [2147483647,2,1,-1],
  [1,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
"""
