# 2564 - Most Profitable Path in a Tree
# Date: 2022-11-14
# Runtime: 1762 ms, Memory: 80.1 MB
# Submission Id: 843261761


from collections import defaultdict, deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        # DFS - build tree
        tree = defaultdict(list)
        parent = defaultdict(int)
        
        stack = [0]
        seen = set([0])
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    tree[node].append(neighbor)
                    seen.add(neighbor)
                    parent[neighbor] = node
                    stack.append(neighbor)
                    
        # BFS - traverse
        ans = float('-inf')
        queue = deque([(0, amount[0])])
        amount[bob] = 0
        while queue:
            bob = parent[bob]
            for _ in range(len(queue)):
                alice, value = queue.popleft()
                if not tree[alice]:
                    ans = max(ans, value)
                for child in tree[alice]:
                    if child == bob:
                        amount[child] //= 2
                    queue.append((child, value + amount[child]))
            amount[bob] = 0

        return ans