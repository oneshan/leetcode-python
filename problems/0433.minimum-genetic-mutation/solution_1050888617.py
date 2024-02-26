# 0433 - Minimum Genetic Mutation
# Date: 2023-09-16
# Runtime: 42 ms, Memory: 16.3 MB
# Submission Id: 1050888617


from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([startGene])
        seen = {startGene}
        
        step = 0
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return step
                for c in 'ACGT':
                    for i in range(len(gene)):
                        candidate = gene[:i] + c + gene[i+1:]
                        if candidate in bank and candidate not in seen:
                            seen.add(candidate)
                            queue.append(candidate)
            step += 1
        return -1