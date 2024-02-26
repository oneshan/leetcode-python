# 1447 - Jump Game IV
# Date: 2023-03-05
# Runtime: 809 ms, Memory: 29 MB
# Submission Id: 909457979


from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        graph = defaultdict(list)
        for idx, num in enumerate(arr):
            graph[num].append(idx)
        
        queue = deque([0])
        seen = {0}
        step = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == n-1:
                    return step
                for child in graph[arr[node]]:
                    if child not in seen:
                        seen.add(child)
                        queue.append(child)
                graph.pop(arr[node])
                for neighbor in (node-1, node+1):
                    if 0 <= neighbor < n and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            step += 1
        return -1