class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        curr = 1
        prev = 1
        for i in range(2, n + 1):
            temp = prev + curr
            prev = curr
            curr = temp
        return curr