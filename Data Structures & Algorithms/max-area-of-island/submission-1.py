class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_sum = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                if (r, c) in visited:
                    continue
                curr_sum = self.dfs(r, c, grid, visited)
                max_sum = max(curr_sum, max_sum)
        return max_sum

    def dfs(self, r, c, grid, visited):
        if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]):
            return 0
        if (r, c) in visited:
            return 0
        if grid[r][c] == 0:
            return 0
        visited.add((r, c))
        curr_sum = 1
        for x, y in [(-1,0), (0, -1), (1, 0), (0, 1)]:
            new_r = x + r
            new_c = y + c
            curr_sum += self.dfs(new_r, new_c, grid, visited)
        return curr_sum
