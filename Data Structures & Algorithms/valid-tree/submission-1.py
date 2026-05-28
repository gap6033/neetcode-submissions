from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = self.build_adj_list(n, edges)
        visited = set()
        start = 0
        dq = deque()
        dq.append((start, None))
        while dq:
            node, source = dq.popleft()
            for dest in adj_list[node]:
                if node == dest:
                    return False
                if dest == source:
                    continue
                if dest in visited:
                    return False
                dq.append((dest, node))
            visited.add(node)
        if len(visited) != n:
            return False
        return True

    def build_adj_list(self, n, edges):
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)

        return adj_list
    


'''
0:[1, 2, 3]
1:[0, 4]
2:[0]
3:[0]
4:[0]
'''