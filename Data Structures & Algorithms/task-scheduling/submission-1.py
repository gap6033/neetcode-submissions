from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_count = {}
        for task in tasks:
            if task not in freq_count:
                freq_count[task] = 0
            freq_count[task] += 1
        
        tasks_to_run = []
        for task in freq_count:
            heapq.heappush(tasks_to_run, (-1 * freq_count[task], 0))
        

        tasks_waiting = deque()

        cpu_cycle = 0
        while tasks_waiting or tasks_to_run:
            while tasks_waiting:
                task_count, last_cycle = tasks_waiting[0]
                if cpu_cycle - last_cycle >= n:
                    heapq.heappush(tasks_to_run, (task_count, last_cycle))
                    tasks_waiting.popleft()
                else:
                    break
            if tasks_to_run:
                task_count, last_cycle = heapq.heappop(tasks_to_run)
                task_count += 1
                cpu_cycle += 1
                last_cycle = cpu_cycle
                if task_count < 0:
                    tasks_waiting.append((task_count, last_cycle))
            else:
                cpu_cycle += 1

        return cpu_cycle
'''
X:2
Y:2
X,Y,
X:2
Y:2

X:1
Y:3
Z:2

Y,X,Z,

X,X,Y,Y,''
54321



Y:2
Z

'''