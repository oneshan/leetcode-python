# 3179 - Maximum Points After Collecting Coins From All Nodes
# Date: 2023-10-29
# Runtime: 5607 ms, Memory: 409 MB
# Submission Id: 1086556648


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        
        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
            
        @ cache
        def recur(node, penalty, prev):
            if 10 ** 4 < 2 ** penalty:
                return 0
            
            res = 0
            choice1 = (coins[node] // (2**penalty)) - k
            choice2 = (coins[node] // ((2**penalty) * 2))
            for child in graph[node]:
                if child == prev:
                    continue
                choice1 += recur(child, penalty, node)
                choice2 += recur(child, penalty + 1, node)
            res += max(choice1, choice2)
            return res
        
        return recur(0, 0, None)