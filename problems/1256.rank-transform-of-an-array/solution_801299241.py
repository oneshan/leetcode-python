# 1256 - Rank Transform of an Array
# Date: 2022-09-16
# Runtime: 730 ms, Memory: 31 MB
# Submission Id: 801299241


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        table = {}
        rank = 1
        for elem in sorted(arr):
            if elem not in table:
                table[elem] = rank
                rank += 1
        return [table[num] for num in arr]