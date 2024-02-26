# 1256 - Rank Transform of an Array
# Date: 2022-10-14
# Runtime: 421 ms, Memory: 31.1 MB
# Submission Id: 822208807


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        table = {}
        rank = 1
        for elem in sorted(arr):
            if elem not in table:
                table[elem] = rank
                rank += 1
        return [table[num] for num in arr]