# 1256 - Rank Transform of an Array
# Date: 2022-09-16
# Runtime: 1072 ms, Memory: 33.8 MB
# Submission Id: 801302536


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        table = {}
        for rank, num in enumerate(sorted(list(set(arr))), 1):
            table[num] = rank

        return [table[num] for num in arr]