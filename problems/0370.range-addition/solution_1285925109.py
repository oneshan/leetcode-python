# 0370 - Range Addition
# Date: 2024-06-12
# Runtime: 136 ms, Memory: 25.1 MB
# Submission Id: 1285925109


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length

        for start, end, val in updates:
            ans[start] += val
            if end < length - 1:
                ans[end+1] -= val

        curr = 0
        for i in range(length):
            curr += ans[i]
            ans[i] = curr
        return ans