# 0274 - H-Index
# Date: 2023-10-29
# Runtime: 52 ms, Memory: 16.6 MB
# Submission Id: 1086629537


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        i = 0
        while i < n and citations[i] > i:
            i += 1
        return i