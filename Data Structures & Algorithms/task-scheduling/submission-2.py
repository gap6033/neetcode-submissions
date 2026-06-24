import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}
        for t in tasks:
            if t not in freq_map:
                freq_map[t] = 0
            freq_map[t] += 1

        max_heap = []
        for t in freq_map:
            heapq.heappush(max_heap, (-freq_map[t]))
        
        cooldown_queue = deque()
        cpu_cycle = 0
        while max_heap or cooldown_queue:
            if cooldown_queue:
                if cooldown_queue[0][-1] <= cpu_cycle:
                    t_freq, _ = cooldown_queue.popleft()
                    heapq.heappush(max_heap, (t_freq))
            task_count = 0
            if max_heap:
                task_count = heapq.heappop(max_heap)
                task_count += 1
            cpu_cycle += 1
            if task_count != 0:
                cooldown_queue.append((task_count, cpu_cycle + n))
        return cpu_cycle

        

'''

0 1  2.  3
X, X, Y, Y

cooldowns = {X:2}
cycles_passed = 0
t = 0
while t < len(tasks):
    task = tasks[t]
    if task not in cooldowns:
        cooldowns[task] = cycles_passed + n
        cycles_passed += 1
    else:
        cooldown = cooldowns[task]
        if cooldown - cycles_passed <= n:
            dq.append(task)
            

    t += 1



'''