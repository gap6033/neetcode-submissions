class Solution:
    dp = {}
    def minOperations(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        operation_count = 0
        
        for num in freq_map:
            count = self.reduce(freq_map[num])
            if count == float('inf'):
                return -1
            operation_count += count
        return operation_count


    def reduce(self, count):
        if count in self.dp:
            return self.dp[count]
        if count < 0:
            return float('inf')
        if count == 0:
            return 0
        min_count = 1 + self.reduce(count - 3)
        min_count = min(min_count, 1 + self.reduce(count - 2))
        self.dp[count] = min_count
        return min_count


        
        


'''
2:5
3:3
4:2

5 % 2 = 2

'''