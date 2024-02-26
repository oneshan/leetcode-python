# 0433 - Minimum Genetic Mutation
# Date: 2022-12-01
# Runtime: 60 ms, Memory: 14 MB
# Submission Id: 852824725


from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([(startGene, 0)])
        seen = {startGene}
        n = 8
        
        while queue:
            gene, step = queue.popleft()
            if gene == endGene:
                return step
            
            for c in 'ACGT':
                for i in range(n):
                    neighbor = gene[:i] + c + gene[i+1:]
                    if neighbor in bank and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, step+1))
        return -1