# 0506 - Relative Ranks
# Date: 2024-05-08
# Runtime: 67 ms, Memory: 17.6 MB
# Submission Id: 1252373855


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        table = {}
        for rank, num in enumerate(sorted(score, reverse=True), 1):
            if rank == 1:
                table[num] = 'Gold Medal'
            elif rank == 2:
                table[num] = 'Silver Medal'
            elif rank == 3:
                table[num] = 'Bronze Medal'
            else:
                table[num] = str(rank)

        return [table[num] for num in score]