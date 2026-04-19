from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        
        output = [nums[dq[0]]]
        l = 0
        r = k
        while r < len(nums):
            l += 1
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)
            while dq[0] < l:
                dq.popleft()
            output.append(nums[dq[0]])
            r += 1
        return output




'''
 0 1 2 3 4 5 6
[1,2,1,0,4,2,6]

[4]
'''