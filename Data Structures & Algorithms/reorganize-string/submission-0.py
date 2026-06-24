import heapq
from collections import deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        for c in s:
            if c not in freq_map:
                freq_map[c] = 0
            freq_map[c] += 1

        max_heap = []
        for c in freq_map:
            heapq.heappush(max_heap, (-freq_map[c], c))
        print(max_heap)
        cooldown = deque()
        output = []
        curr_time = 0
        while max_heap or cooldown:
            if cooldown:
                char, wait_time = cooldown[0]
                if wait_time <= curr_time:
                    heapq.heappush(max_heap, (-freq_map[char], char))
                    cooldown.popleft()
            if max_heap:
                _, char = heapq.heappop(max_heap)
                output.append(char)
                freq_map[char] -= 1
                curr_time += 1
                if freq_map[char] != 0:
                    cooldown.append((char, curr_time + 1))
            else:
                return ""
        return ''.join(output)
            

'''
axyy

yay
'''