# 0433 - Minimum Genetic Mutation
# Date: 2024-06-06
# Runtime: 35 ms, Memory: 16.4 MB
# Submission Id: 1279607968


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        table = defaultdict(set)
        for gene in bank:
            lst_gene = list(gene)
            for i in range(8):
                lst_gene[i] = '*'
                table[''.join(lst_gene)].add(gene)
                lst_gene[i] = gene[i]
        
        queue = deque([startGene])
        seen = set()
        step = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endGene:
                    return step
                lst_gene = list(curr)
                for i in range(8):
                    lst_gene[i] = '*'
                    for next_gene in table[''.join(lst_gene)]:
                        if next_gene in seen:
                            continue
                        seen.add(next_gene)
                        queue.append(next_gene)
                    lst_gene[i] = curr[i]

            step += 1
        return -1