class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        operation_count = 0
        dp = {}
        print(freq_map)

        for num in freq_map:
            count = freq_map[num]
            min_count = 1 + self.reduce(count - 3, dp)
            min_count = min(min_count, 1 + self.reduce(count - 2, dp))
            if min_count == float('inf'):
                return -1
            operation_count += min_count
        return operation_count


    def reduce(self, count, dp):
        if count in dp:
            return dp[count]
        if count < 0:
            return float('inf')
        if count == 0:
            return 0
        min_count = 1 + self.reduce(count - 3, dp)
        min_count = min(min_count, 1 + self.reduce(count - 2, dp))
        dp[count] = min_count
        return min_count


        
        


'''
2:5
3:3
4:2

5 % 2 = 2

'''