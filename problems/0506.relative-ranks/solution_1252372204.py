# 0506 - Relative Ranks
# Date: 2024-05-08
# Runtime: 54 ms, Memory: 17.9 MB
# Submission Id: 1252372204


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        mapping = [(score, idx) for idx, score in enumerate(score)]
        mapping.sort(reverse=True)

        n = len(score)
        rank = [None] * n
        rank[mapping[0][1]] = 'Gold Medal'
        if n > 1:
            rank[mapping[1][1]] = 'Silver Medal'
        if n > 2:
            rank[mapping[2][1]] = 'Bronze Medal'

        for i in range(3, n):
            rank[mapping[i][1]] = str(i+1)

        return rank
