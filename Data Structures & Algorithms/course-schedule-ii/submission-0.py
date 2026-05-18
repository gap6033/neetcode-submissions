from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = {}
        adj_list = {}
        for num in range(numCourses):
            indegrees[num] = 0
            adj_list[num] = set()
        
        for nex, pre in prerequisites:
            indegrees[nex] += 1
            adj_list[pre].add(nex)

        dq = deque()
        for subject in indegrees:
            if indegrees[subject] == 0:
                dq.append(subject)

        output = []
        while dq:
            subject = dq.popleft()
            output.append(subject)
            for node in adj_list[subject]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    dq.append(node)
        if len(output) == numCourses:
            return output

        return []
