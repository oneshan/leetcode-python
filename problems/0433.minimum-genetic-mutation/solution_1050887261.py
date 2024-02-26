# 0433 - Minimum Genetic Mutation
# Date: 2023-09-16
# Runtime: 32 ms, Memory: 16.2 MB
# Submission Id: 1050887261


from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([startGene])
        seen = {startGene}
        
        def get_distance(s1, s2):
            return sum(c1 != c2 for c1, c2 in zip(s1, s2))
        
        step = 0
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return step
                for candidate in bank:
                    if candidate not in seen and get_distance(gene, candidate) == 1:
                        seen.add(candidate)
                        queue.append(candidate)
            step += 1
        return -1