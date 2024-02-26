# 3112 - Count Valid Paths in a Tree
# Date: 2023-10-18
# Runtime: 1623 ms, Memory: 59.2 MB
# Submission Id: 1078379745


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, n+1):
            if not is_prime[i]:
                continue
            for j in range(i+i, n+1, i):
                is_prime[j] = False
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = 0
        def dfs(node, prev):
            nonlocal ans
            if is_prime[node]:
                p0, p1 = 0, 1
            else:
                p0, p1 = 1, 0

            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                non_prime_path, prime_path = dfs(neighbor, node)
                ans += non_prime_path * p1 + prime_path * p0
                if is_prime[node]:
                    p1 += non_prime_path
                else:
                    p0 += non_prime_path
                    p1 += prime_path
            return p0, p1

        dfs(1, 0)
        return ans
