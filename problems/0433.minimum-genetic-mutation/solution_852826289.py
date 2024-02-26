# 0433 - Minimum Genetic Mutation
# Date: 2022-12-01
# Runtime: 39 ms, Memory: 13.9 MB
# Submission Id: 852826289


from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([(startGene, 0)])
        seen = {startGene}
        
        def get_distance(s1, s2):
            return sum(c1 != c2 for c1, c2 in zip(s1, s2))
        
        while queue:
            gene, step = queue.popleft()
            if gene == endGene:
                return step
            
            for candidate in bank:
                if candidate not in seen and get_distance(gene, candidate) == 1:
                    seen.add(candidate)
                    queue.append((candidate, step+1))
        return -1