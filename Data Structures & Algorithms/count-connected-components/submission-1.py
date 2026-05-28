class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = self.build_adj_list(n, edges)
        visited = set()
        dq = deque()
        output = 0
        for i in range(n):
            if i in visited:
                continue
            output += 1
            dq.append((i, None))
            while dq:
                node, source = dq.popleft()
                for dest in adj_list[node]:
                    if dest in visited:
                        continue
                    if dest == source:
                        continue
                    dq.append((dest, node))
                visited.add(node)
        return output
        

    def build_adj_list(self, n, edges):
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)

        return adj_list