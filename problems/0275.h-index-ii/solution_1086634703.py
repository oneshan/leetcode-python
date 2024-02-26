# 0275 - H-Index II
# Date: 2023-10-29
# Runtime: 130 ms, Memory: 23 MB
# Submission Id: 1086634703


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        i = 0
        while i < n and citations[-i-1] > i:
            i += 1
        return i