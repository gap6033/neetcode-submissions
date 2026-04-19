from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        for i in range(k):
            while dq and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])
        
        output = []
        l = 0
        for i in range(k, len(nums)):
            output.append(dq[0])
            if nums[l] == dq[0]:
                dq.popleft()
            l += 1
            while dq and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])
        output.append(dq[0])
        return output


"""
output = [4, 4, 4]
l = 2
i = 4
[4,2,4,0,4,2,6],
[4, 4]
"""