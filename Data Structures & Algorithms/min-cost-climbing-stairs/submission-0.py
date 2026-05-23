class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cost[0]
        curr = cost[1]
        for i in range(2, len(cost)):
            temp = cost[i] + min(prev, curr)
            prev = curr
            curr = temp
        return min(prev, curr)
