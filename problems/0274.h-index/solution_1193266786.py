# 0274 - H-Index
# Date: 2024-03-04
# Runtime: 40 ms, Memory: 17 MB
# Submission Id: 1193266786


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        bucket = [0] * 1001
        for citation in citations:
            bucket[citation] += 1

        count = 0
        for i in range(1000, -1, -1):
            count += bucket[i]
            if count >= i:
                return i
        return 0