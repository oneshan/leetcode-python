# 0433 - Minimum Genetic Mutation
# Date: 2024-06-06
# Runtime: 30 ms, Memory: 16.5 MB
# Submission Id: 1279612625


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([startGene])
        step = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endGene:
                    return step
                for i in range(8):
                    for ch in 'ACGT':
                        next_gene = curr[:i] + ch + curr[i+1:]
                        if next_gene not in bank:
                            continue
                        queue.append(next_gene)
                        bank.remove(next_gene)
            step += 1
        return -1