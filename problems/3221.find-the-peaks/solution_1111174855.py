# 3221 - Find the Peaks
# Date: 2023-12-03
# Runtime: 56 ms, Memory: 16.2 MB
# Submission Id: 1111174855


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        n = len(mountain)
        for i in range(1, n-1):
            if mountain[i-1] < mountain[i] and mountain[i] > mountain[i+1]:
                ans.append(i)
        return ans