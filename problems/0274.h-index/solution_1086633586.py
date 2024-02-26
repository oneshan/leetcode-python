# 0274 - H-Index
# Date: 2023-10-29
# Runtime: 48 ms, Memory: 16.6 MB
# Submission Id: 1086633586


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper = [0] * (n+1)
        for c in citations:
            paper[min(c, n)] += 1
        
        h_index, curr_sum = n, paper[n]
        while h_index > curr_sum:
            h_index -= 1
            curr_sum += paper[h_index]
        return h_index